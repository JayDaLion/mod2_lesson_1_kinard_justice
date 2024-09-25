"""#movie night

mood = input("How are you feeling today?: ").lower()
weather = int(input("Whats the weather in degrees?: "))
weather_type = ""

if 75 <=  weather <= 99:
        weather_type = "sunny"
else :
        weather_type != "sunny"



if mood == "happy" and weather_type == "sunny": 
        print ("Try a comedy")
elif mood == "happy" and weather_type != "sunny":
        print("Maybe in the mood for romantic movie?")
elif mood == "sad":
        print ("Drama should make you ponder elsewhere")
else:
        print("Adventure is calling")
"""

"""#Temp and clothing
temperature = int(input("What is the temperature outside?:" ))
event_type = input("Whats the occusion(Formal,Casual,etc.): ").lower()
if  temperature <= 15 and event_type == "casual":
    print("try a cozy sweater and jeans")
elif  temperature <= 15 and event_type == "formal":
    print("try a warm formal suit")
elif  temperature > 15 and event_type == "formal":
    print("Light formal suit should do fine")
else:
    print("t-shirts and shorts")"""

"""#discounts
plays_sports = input("Are you on a sports team?(Yes or No): " ).strip().lower()
drama_club_member = input ("Are you a member of the Drama club?(Yes or No): " ).strip().lower
grade_is = input("Whats your letter grade?: ").lower()
discount =  ""

if plays_sports == "Yes":
    answer = True
elif plays_sports == "No":
    answer = False
else:
    answer = None

if drama_club_member == "Yes":
    answer = True
elif drama_club_member == "No":
    answer = False
else:
    answer = None





if plays_sports == True and grade_is ("A"):
    discount = "Your discount is 20%"
elif plays_sports == False and grade_is ("A"):
    discount = "Your discount is 10%"
else:
 drama_club_member == "yes" and grade_is == "B"
discount = "Your discount is 15%"
print(discount)"""  

"""#quick age check
user_age = int(input("How old are you?: "))

if user_age >= 18: print("You can drive") 
else: print("Not yet you cant enter!")"""

"""#food choice
meal_type = input("Vegan or non-Vegan: ").strip().lower()
diet_restrictions = input("Sugar-free or regular: ").strip().lower()
if meal_type == "vegan" and diet_restrictions == "sugar-free":
        print("Fruit Salad... Yummy yummy")
elif meal_type == "vegan" and diet_restrictions == "regular": 
        print("Try a Veggie cake")
elif meal_type != "Vegan" and diet_restrictions == "sugar-free":
        print("Some Sugar free ice cream shall help")
else:
        print("Try a brownie")"""