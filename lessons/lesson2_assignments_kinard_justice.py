"""#buggy code
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")"""

"""#greatest showdown

number = (input("Enter a set of numbers seperated by spaces: "))
number_list = list(map(int, number.split()))
small_num = min(number_list)
big_num = max(number_list)

print ("The smallest number is:",small_num)
print ("the biggest number is:",big_num)"""

"""#leapyear or not
year =  int(input("What year do you want to test?: "))
is_leapyear = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(is_leapyear)"""