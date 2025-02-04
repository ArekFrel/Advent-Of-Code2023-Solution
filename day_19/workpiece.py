class AAA:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __getitem__(self, item):
        match item:
            case 'a':
                return self.a
            case 'b':
                return self.b
            case 'c':
                return self.c
            case _:
                return 0




aaa = AAA(1,2,3)

print(aaa['a'])