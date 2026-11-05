from typing import Any

from arbiter.interface.user_info import ask_user_info, show_user_info


def run_dashboard() -> None:
    users: list[dict[str, Any]] = []
    while True:
        print("\n1. Add user\n2. View users\n3. Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            users.append(ask_user_info())
            print("Saved.")
        elif choice == "2":
            if not users:
                print("No users yet.")
            for info in users:
                print()
                show_user_info(info)
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
