import os
import json

os.makedirs("data", exist_ok=True)

rows = [
    {
        "id": "ex1",
        "inputs": {"case_text": "Donoghue v Stevenson established the modern law of negligence and duty of care."},
        "must_have": ["Donoghue", "duty of care"],
        "task": "summarize",
    }
]

with open("data/seed.jsonl", "w") as f:
    for r in rows:
        f.write(json.dumps(r) + "\n")

print("Seeded data/seed.jsonl")
