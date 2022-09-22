class DualNum:
    def __init__(self, real, dual=0.0):
        self.real = float(real)
        self.dual = float(dual)

    def __repr__(self) :
        return f"DualNum({self.real}, {self.dual})"

    def __add__(self, other):
        other = other if isinstance(other, DualNum) else DualNum(other)
        return DualNum(self.real + other.real, self.dual + other.dual)

    def __mul__(self, other):
        other = other if isinstance(other, DualNum) else DualNum(other)
        return DualNum(self.real * other.real, self.real * other.dual + self.dual * other.real)

    def __pow__(self,other):
        assert isinstance(other, (int, float)), "only support for int/float powers"
        return DualNum(pow(self.real, other) , other * self.dual * pow(self.real, other - 1))

    #def exp(self):
    #    realexp = math.exp(self.real)
    #    return DualNum(realexp, self.dual * realexp)

    def __neg__(self):
        return self * (-1)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return other + (-self)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self * other**(-1)

    def __rtruediv__(self, other):
        return other * self ** (-1)
