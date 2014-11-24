#Daniel Ogunlana
#18-11-2014
#Classroom starters making calculate functions

#Define a function
def calculate_basic_pay(hours,pay):
    basic_pay = hours * pay
    return basic_pay

def calculate_overtime_pay(hours,pay):
    overtime_hours = hours -40
    overtime_pay = pay * 1.5
    total_overtime = overtime_hours * overtime_pay
    basic_pay = 40* pay
    total_pay = basic_pay + total_overtime
    return total_pay

def calculate_total_pay(hours,pay):
    if hours <= 40:
        total_pay = calculate_basic_pay(hours,pay)
    else:
        total_pay = calculate_overtime_pay(hours,pay)
    return total_pay

def work_details():
    hours = int(input("Please enter the amount of hours that you worked this week: "))
    pay = float(input("Please enter your pay rate: "))
    return hours,pay

def display_total_pay(total_pay):
    print("You will be paid {0}".format(total_pay))
    

def calculate_pay():
    hours,pay = work_details()
    total_pay = calculate_total_pay(hours,pay)
    display_total_pay(total_pay)

#Main Program
calculate_pay()
    
          



