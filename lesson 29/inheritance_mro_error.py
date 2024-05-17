class X: ...
class Y: ...

class A(X, Y): ...
class B(Y, X): ...


class MyMRO(type):
    def mro(cls):
        return (cls, X, Y, A, B, object)


class G(A, B, metaclass=MyMRO): ...

g = G()
print(*[c.__name__ for c in G.mro()], sep=' -> ')

# g = G()
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases X, Y

# class X: ...
# class Y(X): ...
# class A(X, Y): ...

# a = A()
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases X, Y