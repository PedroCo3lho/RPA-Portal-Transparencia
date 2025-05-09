import json
from pathlib import Path

def serialize_to_json(data, screenshot_b64, search, filters, error=None):
    Path("data/outputs").mkdir(parents=True, exist_ok=True)
    output = {
        "pesquisa": search,
        "filtros": filters if filters else None,
        "dados": data if data else None,
        "screenshot_base64": screenshot_b64 if screenshot_b64 else None,
        "erro": error if error else None
    }
    output = {key: value for key, value in output.items() if value is not None}
    with open(f"data/outputs/{search}.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
