#Daniel Ogunlana
#18-11-2014
#Classroom starters making calculate functions

#define a function
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

def work_details

def display_total_pay

def calculate_pay



