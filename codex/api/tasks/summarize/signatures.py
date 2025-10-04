import dspy


class ExtractBrief(dspy.Signature):
    """Extract key elements from a long case text."""
    case_text: str
    citation: str
    issues: str
    holding: str
    reasoning: str


class CondenseNarrative(dspy.Signature):
    """Condense a structured brief into a coherent narrative."""
    brief: str
    narrative: str


class DenseBullets(dspy.Signature):
    """Produce dense bullet points from a narrative."""
    narrative: str
    bullets: list[str]
