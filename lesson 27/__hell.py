class SpecialInt(int):

    def __init__(self, i) -> None:
        self.i = i
        super().__init__()

    def __add__(self, other):
        if isinstance(other, str):
            return str(self.i) + other
        return super().__add__(other)
    
    def __len__(self):
        return len(str(self.i))
    

s = SpecialInt(5)
print(s + 'hello')
# print(s + 5)

d = SpecialInt(1231246348681762)
print(len(d))

print(s + 5)