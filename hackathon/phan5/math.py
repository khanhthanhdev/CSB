import random
import operator
print("== FREAKING MATH CONSOLE ==")
print("Give correct answers to get scroes.")
def randomOperatorAndNumber():
    operators = {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv,
    }
    number1 = random.randint(1,50)
    number2 = random.randint(1,50)
    ope = random.choice(list(operators.keys()))
    answer = operators.get(ope)(number1,number2)   
    return answer
def question():
    answer = randomOperatorAndNumber()
    dapan = float(input())
    return dapan == answer
def answerQuestion():
    score = 0
    for i in range(10):
        if question() ==True:
            score += 1
            print("dung \n")
        else:
            print("sai \n")
    print(f"Your total score is {score}")



answerQuestion()








