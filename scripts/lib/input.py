def ask_bool(msg: str) -> bool:
    answer = input(f"{msg} [Y/n] ").strip().lower()
    check = answer in ["", "y", "n", "yes", "no"]
    return answer in "yes" if check else ask_bool()