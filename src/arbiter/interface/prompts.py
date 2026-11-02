def ask_text(label: str, required: bool = True) -> str:
    while True:
        value = input(f"{label}: ").strip()
        if value or not required:
            return value
        print("This field is required.")


def ask_int(label: str, minimum: int | None = None, maximum: int | None = None) -> int:
    while True:
        try:
            value = int(input(f"{label}: ").strip())
        except ValueError:
            print("Enter a whole number.")
            continue
        if minimum is not None and value < minimum:
            print(f"Must be at least {minimum}.")
        elif maximum is not None and value > maximum:
            print(f"Must be at most {maximum}.")
        else:
            return value


def ask_float(label: str, minimum: float | None = None) -> float:
    while True:
        try:
            value = float(input(f"{label}: ").strip())
        except ValueError:
            print("Enter a number.")
            continue
        if minimum is not None and value < minimum:
            print(f"Must be at least {minimum}.")
        else:
            return value


def ask_choice(label: str, options: list[str]) -> str:
    for i, option in enumerate(options, start=1):
        print(f"  {i}. {option}")
    while True:
        pick = input(f"{label} (1-{len(options)}): ").strip()
        if pick.isdigit() and 1 <= int(pick) <= len(options):
            return options[int(pick) - 1]
        print("Invalid choice.")
