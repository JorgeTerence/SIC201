def ordered_list(l: list):
    return [f"{i} - {item}" for i, item in enumerate(l, start=1)]

def unordered_list(l: list):
    return [f"- {item}" for item in l]