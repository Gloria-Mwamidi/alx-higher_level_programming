#!/usr/bin/python3
if __name__ == "__main__":
    """Prints all names defined by the compiled module"""
    import hidden_4
    name = dir(hidden_4)
    for names in names:
        if names[:2] != "__":
            print(name)
