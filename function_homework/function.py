# 실습2

def gugudan_odd():
    i=1
    while i< 10:
        for j in range(1, 10):
            print("%d * %d" %(i,j))
        i += 2

def gugudan_even():
    i=2
    while i< 10:
        for j in range(1, 10):
            print("%d * %d" %(i,j))
        i += 2

def gugudan_if(num):
    if(num % 2 ==0):
        gugudan_even()
    else:
        gugudan_odd()

gugudan_if(5)
gugudan_if(4)

# 실습3

def gugudan_until(num):
    i=1
    while i< num:
        for j in range(1, 10):
            print("%d * %d" %(i,j))
        i += 1

gugudan_until(3)

