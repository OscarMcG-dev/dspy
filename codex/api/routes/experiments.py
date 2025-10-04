from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Any, Dict, List, Optional

from api.tasks.summarize.pipeline import Pipeline
from api.tasks.summarize.metrics import coverage_brevity_metric
from api.services.dspy_runner import compile_program, run_inference


router = APIRouter()


class CompileRequest(BaseModel):
    task: str
    trainset: List[Dict[str, Any]]
    trials: Optional[int] = 2


class CompileResponse(BaseModel):
    program_id: str


class InferenceRequest(BaseModel):
    program_id: str
    inputs: Dict[str, Any]


PROGRAMS: Dict[str, Any] = {}


@router.post("/compile", response_model=CompileResponse)
def compile_endpoint(req: CompileRequest):
    if req.task != "summarize":
        raise HTTPException(status_code=400, detail="Unsupported task")
    prog = compile_program(Pipeline, req.trainset, coverage_brevity_metric, trials=req.trials or 2)
    pid = "prog_summarize_v1"
    PROGRAMS[pid] = prog
    return {"program_id": pid}


@router.post("/run")
def run_endpoint(req: InferenceRequest):
    if req.program_id not in PROGRAMS:
        raise HTTPException(status_code=404, detail="Program not found")
    prog = PROGRAMS[req.program_id]
    out = run_inference(prog, **req.inputs)
    return {"output": out}
