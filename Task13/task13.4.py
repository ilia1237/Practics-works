from datetime import datetime

def append_log(message: str, path="demo/log.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Режим "a" (append) гарантує, що попередні дані не зітруться
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")
        
    with open(path, "r", encoding="utf-8") as f:
        return f.read()