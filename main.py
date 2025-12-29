def main(input: str) -> str:
    parts = input.strip().split()

    if len(parts) != 3:
        raise Exception("Invalid expression format")

    a_str, operator, b_str = parts

    if not a_str.isdigit() or not b_str.isdigit():
        raise Exception("Operands must be integers")

    a = int(a_str)
    b = int(b_str)

    if not (1 <= a <= 10 and 1 <= b <= 10):
        raise Exception("Numbers must be from 1 to 10")

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a // b
    else:
        raise Exception("Invalid operator")

    return str(result)


if __name__ == "__main__":
    user_input = input()
    print(main(user_input))
