import string
from exe5_1 import Complex


class Token:

    def __init__(self, tokenType, tokenValue):
        self.tokenType = tokenType
        self.tokenValue = tokenValue

class Calculator:

    def __init__(self):
        self.idx = 0
        #               0         1        2      3      4       5         6
        self.TYPE = ["Number", "Plus", "Minus", "Mul", "Div", "LEFTPP", "RIGHTP"]


    def calculate(self, equation):
        return self.expr(equation)

    def expr(self, equation):
        left = self.term(equation)

        while(True):
            op = self.token(equation)

            if(op.tokenType == self.TYPE[1] or op.tokenType == self.TYPE[2]):
                self.idx += 1

                if(op.tokenType == self.TYPE[1]):
                    left += self.term(equation)
                elif(op.tokenType == self.TYPE[2]):
                    left -= self.term(equation)
            
            else:
                return left



    def getNumber(self, equation):
        intv = 0
        while(self.idx < len(equation) and equation[self.idx].isnumeric()):
            intv = 10 * intv + int(equation[self.idx])
            self.idx += 1
        

        return intv

    def token(self, equation):
        while(self.idx < len(equation) and equation[self.idx] in string.whitespace):
            self.idx += 1
        
        if(self.idx < len(equation) and equation[self.idx].isnumeric()):
            return Token(self.TYPE[0], self.getNumber(equation))
        elif(self.idx < len(equation)):
            if(equation[self.idx] == '+'):
                return Token(self.TYPE[1], 0)
            if(equation[self.idx] == '-'):
                return Token(self.TYPE[2], 0)
            if(equation[self.idx] == '*'):
                return Token(self.TYPE[3], 0)
            if(equation[self.idx] == '/'):
                return Token(self.TYPE[4], 0)
            if(equation[self.idx] == '('):
                return Token(self.TYPE[5], 0)
            if(equation[self.idx] == ')'):
                return Token(self.TYPE[6], 0)
        
        return Token(self.TYPE[0], 0)
    
    def factor(self, equation):
        val = 0
        tok = self.token(equation)

        if(tok.tokenType == self.TYPE[0]):
            val = tok.tokenValue
        elif(tok.tokenType == self.TYPE[5]):
            self.idx += 1
            val = self.expr(equation)

            rtok = self.token(equation)

            assert rtok.tokenType == self.TYPE[6]

            self.idx += 1
        
        return val
    
    def term(self, equation):
        leftOp = self.factor(equation)

        while(True):
            tok = self.token(equation)

            if(tok.tokenType == self.TYPE[3] or tok.tokenType == self.TYPE[4]):
                self.idx += 1
                if(tok.tokenType == self.TYPE[3]):
                    leftOp *= self.factor(equation)
                elif(tok.tokenType == self.TYPE[4]):
                    leftOp /= self.factor(equation)
            else:
                return leftOp 


if __name__ == "__main__":
    c1 = Complex(1, 2)
    c2 = Complex(3, -4)
    c3 = Complex(-2, 2)
    s = str(c1) + str(c2) + str(c3)
    cal = Calculator()
    print(cal.calculate(s))