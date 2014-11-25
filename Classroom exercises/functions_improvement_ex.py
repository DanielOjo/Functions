#Daniel Ogunlana
#Functions improvement exercise
#Times-table tester
import random

#Functions

def time_table():
    testTable = input("Which times-table do you want to be tested on? ")
    testTable = int(testTable)
    return testTable

def questions():
    for questions in range(1,6):
        Num1 = testTable
        Num2 = random.randrange(2,13)
        Ans = Num1 * Num2
        UserAnswer = input(str(Num1) + ' x ' + str(Num2) + ' = ? ')
        UserAnswer = int(UserAnswer)
    return Num1,Num2,Ans,UserAnswer

def user_true_or_false(UserAnswer,Ans):
    if UserAnswer == Ans:
        print('Well done, you got the correct answer!')
        print()
    else:
        print('Sorry, you got the answer wrong. The correct answer is',Ans)
        print()

#Main program
print("Times-table tester")
print()
testTable = input("Which times-table do you want to be tested on? ")
testTable = int(testTable)
for questions in range(1,6):
    Num1 = testTable
    Num2 = random.randrange(2,13)
    Ans = Num1 * Num2
    UserAnswer = input(str(Num1) + ' x ' + str(Num2) + ' = ? ')
    UserAnswer = int(UserAnswer)
    if UserAnswer == Ans:
        print('Well done, you got the correct answer!')
        print()
    else:
        print('Sorry, you got the answer wrong. The correct answer is',Ans)
        print()
              
