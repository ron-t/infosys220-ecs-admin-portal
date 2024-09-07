split_by_comma = lambda s : s.split(",")

def split_to_pair(s: str) -> list[str, str]:
    return s.split("__", 1)