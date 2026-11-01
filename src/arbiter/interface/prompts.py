def ask_text(lable: str , required: bool = True) -> str:
    while True:
        value = input(f"{lable}: ").strip()
        if value or not required:
            return value
        print("this field is required")
