import json

def test_json_roundtrip(data: dict, path="demo/students.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    with open(path, "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
        
    is_identical = (data == loaded_data)
    return loaded_data, is_identical