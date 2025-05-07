import json
from pathlib import Path

def serialize_to_json(data, screenshot_b64, search):
    Path("data/outputs").mkdir(parents=True, exist_ok=True)
    output = {
        "pesquisa": search,
        "dados": data,
        "screenshot_base64": screenshot_b64
    }
    with open(f"data/outputs/{search}.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
