def analyze_numbers(path="demo/numbers.txt"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            # Перетворюємо токени на числа (float, якщо є крапка, інакше int)
            nums = [float(x) if "." in x else int(x) for x in content.split()]
            
            if not nums:
                return "Файл порожній."
                
            return {
                "sum": sum(nums),
                "count": len(nums),
                "max": max(nums),
                "min": min(nums)
            }
    except FileNotFoundError:
        return f"Помилка: файл '{path}' не знайдено."
    except ValueError as e:
        return f"Помилка формату даних у файлі: {e}"