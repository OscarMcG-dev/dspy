import dspy
from .signatures import ExtractBrief, CondenseNarrative, DenseBullets


class Pipeline(dspy.Module):
    def __init__(self) -> None:
        super().__init__()
        self.extract = dspy.Predict(ExtractBrief)
        self.condense = dspy.Predict(CondenseNarrative)
        self.dense = dspy.Predict(DenseBullets)

    def forward(self, case_text: str):
        brief = self.extract(case_text=case_text)
        brief_text = "\n".join(
            [
                f"Citation: {brief.citation}",
                f"Issues: {brief.issues}",
                f"Holding: {brief.holding}",
                f"Reasoning: {brief.reasoning}",
            ]
        )
        condensed = self.condense(brief=brief_text)
        dense = self.dense(narrative=condensed.narrative)
        return {
            "brief": brief_text,
            "narrative": condensed.narrative,
            "bullets": dense.bullets,
        }
