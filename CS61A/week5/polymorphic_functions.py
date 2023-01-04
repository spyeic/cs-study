
class Bear:
    def __init__(self):
        self.__repr__ = lambda: "New_Bear()"
        self.__str__ = lambda: "new bear function"

    def __repr__(self):
        return "Bear()"

    def __str__(self):
        return "a bear function"


bear = Bear()
print(bear)
print(str(bear))
print(repr(bear))
print(bear.__str__())
print(bear.__repr__())
