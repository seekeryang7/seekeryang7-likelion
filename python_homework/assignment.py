# '''
# 과제 1. 별찍기 (4월 20일까지)
# - 아래와 같이 * 을 출력 하는 프로그램을 만들어보세요
# **********
# *********
# ********
# *******
# *****
# ****
# ***
# **
# *

# 과제1
print("과제1")
for a in range(10):
    print ('*'*(9-(a)))


# 과제 2. 구구단 (4월 20일까지)
# - 구구단 2단을 출력해보세요!
print("과제2")
for a in range(9):
    print(2*(a+1), end=' ')

# 과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요. (4월 20일까지)
print("과제3")
three = 1
sum = 0
while three < 1000:
    three = three + 1
    if three % 3 == 0:
        sum = sum + three
    if three == 999:
        print(sum)
        break    


# 과제 4. for 문을 활용하여 멋사 학생들의 평균 점수를 구해보세요. (4월 20일까지)
print("과제4")
mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
sum = 0
for score in mutsa_scores:
    sum = sum + score
    if score == mutsa_scores[-1]:
        print(sum/len(mutsa_scores))

# 과제 5. input.py 문제 2개 풀기 (4월 20일까지)

# 과제 6. HTML / CSS 페이스북 모바일 클론코딩 (4월 27일까지)
# - 이미지 자율
# - 까먹기전에 해주세요~
