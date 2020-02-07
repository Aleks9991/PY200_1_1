class A:
    a = 1
    def __init__(self, a=None):
        self.a = a

    def print_a(self):
        print('Attr <a> from object <{}> = {}'.format(self.__class__.__name__, self.a))

    @classmethod
    def other_print_a(cls):
        print('Attr <a> from object <{}> = {}'.format(cls.__class__.__name__, cls.a))

a = A(100)
a.print_a()
a.other_print_a()

class B:
    def __init__(self, b):
        self.b = b