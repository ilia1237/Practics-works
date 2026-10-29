def wc(path="demo/text.txt"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
            lines = text.splitlines()
            return {
                "lines": len(lines),
                "words": len(text.split()),
                "chars": len(text)
            }
    except FileNotFoundError:
        return f"Помилка: файл '{path}' не знайдено."