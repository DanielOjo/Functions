#Daniel Ogunlana
#02/01/15
#Functions development exercise Task 1

def user_information():
    hours = int(input("Please enter the number of hours :"))
    minutes = int(input("Please enter the number of minutes :"))
    seconds = int(input("Please enter the number of seconds : "))
    return hours,minutes,seconds

def calculation(hours,minutes,seconds):
    hours = hours/3600
    minutes = minutes/60
    total = hours + minutes + seconds
    return total

def answer(total):
    print("The total amount of seconds is {0}".format(total))
           
def main():
    hours,minutes,seconds = user_information()
    total = calculation(hours,minutes,seconds)
    total_answer = answer(total)

#main program
main()

