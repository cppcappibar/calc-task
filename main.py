def main(input: str) -> str:
    parts = input.strip().split()

    if len(parts) != 3:
        raise Exception("Недопустимый формат выражения")

    a_str, operator, b_str = parts

    if not a_str.isdigit() or not b_str.isdigit():
        raise Exception("Операнды должны быть целыми числами")

    a = int(a_str)
    b = int(b_str)

    if not (1 <= a <= 10 and 1 <= b <= 10):
        raise Exception("Операнды должны быть в диапазоне от 1 до 10")

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a // b
    else:
        raise Exception("Недопустимый оператор")

    return str(result)

if __name__ == "__main__":
    try:
        user_input = input()
        print(main(user_input))
    except Exception:
        print("throws Exception")
