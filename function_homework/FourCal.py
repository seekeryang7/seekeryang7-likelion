# 과제1

class FourCal:
    def __init__(self, name, age, univ):
        self.name = name
        self.age = age
        self.univ = univ
        self.add_num = 0
        self.sub_num = 0
        self.mul_num = 0
        self.div_num = 0
    def add(self, num1, num2):
        self.add_num +=1
        return num1+num2
    def sub(self, num1, num2):
        self.sub_num +=1    
        return num1-num2
    def mul(self, num1, num2):
        self.mul_num +=1
        return num1*num2
    def div(self, num1, num2):
        self.div_num +=1
        # if(num2 == 0):
        #     print('0으로 나눌 수 없습니다')
        #     return None
        return num1/num2
    def showcount(self):
        print('덧셈: %s' %self.add_num)
        print('뺄셈: %s' %self.sub_num)
        print('곱셈: %s' %self.mul_num)
        print('나눗셈: %s' %self.div_num)

calculator1 = FourCal('양현식',27,'korea')
print(calculator1.add(3,4))
print(calculator1.sub(2,1))
print(calculator1.add(234,3))
print(calculator1.mul(2,3))
print(calculator1.mul(3,5))
print(calculator1.div(3,2))

print(calculator1.showcount())
