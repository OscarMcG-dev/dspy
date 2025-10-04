import os
import dspy
import mlflow
from typing import Any, Dict, List, Type
from dspy import Example
from dspy.optimize import MIPROv2


def configure_lm() -> None:
    model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    dspy.settings.configure(lm=dspy.OpenAI(model=model_name))


def compile_program(pipeline_cls: Type[dspy.Module], trainset: List[Dict[str, Any]], metric_fn, trials: int = 3):
    mlflow.dspy.autolog(log_traces=True, log_traces_from_compile=True)
    configure_lm()
    program = pipeline_cls()
    # Expect each row: {"inputs": {..}, ...}
    ds = []
    for row in trainset:
        inputs = row.get("inputs", {})
        ex = Example(**row)
        # Determine input field names from provided inputs dict
        input_fields = list(inputs.keys())
        ds.append(ex.with_inputs(*input_fields))

    optimizer = MIPROv2(
        metric=metric_fn,
        num_trials=trials,
        max_bootstrapped_demos=4,
        max_labeled_demos=4,
    )
    return optimizer.compile(program, trainset=ds)


def run_inference(program: dspy.Module, **kwargs):
    return program(**kwargs)
