class A:
    size = 5

class B (A):
    pass

class M:
    def print_size(self):
        print("Size = ",self.size)

class C(A, M):
    pass

class D(B, M):
    pass

c = C()
c.print_size()