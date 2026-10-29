import csv

def process_students_csv(path="demo/students.csv"):
    scores_dict = {}
    valid_scores = []
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None) # пропускаємо рядок заголовків
            
            for row in reader:
                if len(row) < 2:
                    continue
                surname, score_str = row[0].strip(), row[1].strip()
                try:
                    score = float(score_str) if "." in score_str else int(score_str)
                    scores_dict[surname] = score
                    valid_scores.append(score)
                except ValueError:
                    print(f"Попередження: некоректний бал '{score_str}' для студента {surname}")
                    
        avg_score = sum(valid_scores) / len(valid_scores) if valid_scores else 0.0
        return scores_dict, avg_score
        
    except FileNotFoundError:
        return f"Файл '{path}' не знайдено.", 0.0