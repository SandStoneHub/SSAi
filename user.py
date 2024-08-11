import json

def add(id: int, prompt: str):
    json_data = {id: prompt}

    with open("user.json", "a", encoding='utf8') as file:
        json.dump(json_data, file, indent=2, ensure_ascii=False)
        file.write(',\n')