
class A:
    a = 1

    def print_a(self):
        self.a = 2
        print(self.a)


A().print_a()
print(A.a)
