from typing import Dict, Any


def coverage_brevity_metric(pred: Dict[str, Any], ex: Dict[str, Any]) -> float:
    """Score coverage of must-have tokens with brevity penalty.

    pred: expects keys narrative (str) and bullets (list[str])
    ex: expects key must_have (list[str])
    """
    narrative_text = pred.get("narrative", "")
    bullets_list = pred.get("bullets", []) or []
    text = (narrative_text + " " + " ".join(bullets_list)).lower()
    must = [t.lower() for t in ex.get("must_have", [])]
    coverage = sum(int(t in text) for t in must) / max(1, len(must))
    length = max(1, len(text))
    penalty = max(0.0, (length - 1200) / 1200)
    return max(0.0, coverage - 0.25 * penalty)
