def sort_and_save_numbers(src_path="demo/numbers.txt", dest_path="demo/sorted_numbers.txt"):
    try:
        with open(src_path, "r", encoding="utf-8") as f:
            nums = sorted([float(x) if "." in x else int(x) for x in f.read().split()])
    except FileNotFoundError:
        return f"Вихідний файл '{src_path}' не знайдено."
    except ValueError as e:
        return f"Помилка у даних вихідного файлу: {e}"

    try:
        with open(dest_path, "x", encoding="utf-8") as f:
            f.write(" ".join(map(str, nums)))
        return f"Дані успішно відсортовано та записано у '{dest_path}'."
    except FileExistsError:
        return f"Попередження: файл '{dest_path}' вже існує! Перезапис скасовано."