class Fraction:
    def __init__(self,top,bottom):
        self.num=top
        self.den=bottom

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum,newden)

    def show(self):
        print(self.num,"/",self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

myfraction = Fraction(3,5)
myfraction.show()
print(myfraction)

f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3= f1+f2
print(f3)