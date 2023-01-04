
class A:
    def __add__(self, other):
        print("__add__ in class A")

    def __radd__(self, other):
        print("__radd__ in class A")


class B:
    def __add__(self, other):
        print("__add__in class B")

    def __radd__(self, other):
        print("__radd__ in class B")
