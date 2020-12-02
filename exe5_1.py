import math

class Complex:

    def __init__(self, real = 0, img = 0):
        self.real = real
        self.img = img
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.img - other.img)
    
    def __mul__(self, other):
        return Complex(self.real * other.real - self.img*other.img, self.real * other.img + other.real * self.img)

    def __div__(self, other):
        a, b, c, d = self.real, self.img, other.real, other.img
        r = float(c**2 + d**2)
        return Complex((a*c+b*d)/r, (b*c-a*d)/r)
    
    def __abs__(self):
        return math.sqrt(self.real**2 + self.img**2)
    
    def __neg__(self):
        return Complex(-self.real, - self.img)
    
    def __eq__(self, other):
        return self.real == other.real and other.img == self.img
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        if(self.img > 0):
            return "{} + {}i".format(self.real, self.img)
        else:
            return "{} {}i".format(self.real, self.img)
    
    def __repr__(self):
        return 'Complex ' + str(self)
    
    def __pow__(self, power):
        tan = math.atan(self.img/self.real)
        tan *= power
        r = abs(self)**power
        return Complex(round(r*math.cos(tan)), round(r*math.sin(tan)))


if __name__ == "__main__":
    c = Complex(3,-5)
    print(c**4)