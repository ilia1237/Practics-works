def create_and_read_table(n: int, path="demo/table.txt"):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{'N':<5}{'Square':<10}{'Cube':<10}\n")
        f.write("-" * 25 + "\n")
        for i in range(1, n + 1):
            f.write(f"{i:<5}{i**2:<10}{i**3:<10}\n")
            
    with open(path, "r", encoding="utf-8") as f:
        return f.read()