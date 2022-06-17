def isstring_int(arg: str):
    try:
        int(arg)
        return True
    except ValueError:
        return False
