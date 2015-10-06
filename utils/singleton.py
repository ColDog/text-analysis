def singleton(cls):
    instances = {}
    if cls not in instances:
        instances[cls] = cls()
    return instances[cls]
