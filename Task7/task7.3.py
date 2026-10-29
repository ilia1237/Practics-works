s = "А роза упала на лапу Азора"

cleaned = "".join(c.lower() for c in s if c.isalnum())
is_palindrome = cleaned == cleaned[::-1]

print("так" if is_palindrome else "ні")