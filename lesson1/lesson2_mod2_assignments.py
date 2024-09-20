"""#Traffic Light Sim
traffic_light_color = input("What color is the light? ")
if traffic_light_color == "green" or traffic_light_color == "Green" or traffic_light_color == "GREEN":
    print("Light is green, GO!")
elif traffic_light_color == "yellow" or traffic_light_color == "Yellow" or traffic_light_color == "YELLOW" :
    print ("Be ready to stop, Light is yellow")
elif traffic_light_color == "red" or traffic_light_color == "Red" or traffic_light_color == "RED":
    print ("Light is RED STOP!!!")
else:
    print("thats not a stoplight color")"""

"""#movie age restriction
#movie ratings
guest_age = int(input("How old are you?"))
movie_rating = input("What is the rating of the movie you would like to watch?").lower()
## trying to figure out how to single out if the age is a number or a string and vice versa for the rating

if movie_rating == "G" or movie_rating == "g":
    print("Enjoy the movie!")
elif movie_rating == "Pg" or movie_rating == "PG" or movie_rating == "pg" and guest_age >= 8:
    print ("Enjoy the movie!")
elif guest_age != 8: 
    print("You need an adult to watch")
elif movie_rating == "pg13" or movie_rating == "PG13" or movie_rating == "PG-13" or movie_rating == "pg-13" and guest_age >= 13:
    print("Enjoy the movie")
elif guest_age != 13: 
    print("You need an adult to watch")   
elif movie_rating == "r" or movie_rating == "R"  and guest_age >= 17:
    print("Enjoy the movie")
elif guest_age != 17: 
    print("You need an adult to watch")
else:
    print("Either not a number or rating combination try again")"""

"""#Temp and clothing
temperature = int(input("What is the temperature outside?:" ))
if 0 <= temperature <= 40:
    print("It's freezing out, grab a long sleeve tee, some thermal undergarments(tee and bottoms), and a jacket and boots. You're gonna need it!")
elif 40 <= temperature <= 60:
    print("It's pretty chilly out, grab a light sweater, thermal leggings, and a light jacket and scarf. It'll prove useful!")
elif 60 <= temperature <= 70:
    print("Average temps out, Blue jeans, A white tee, and your favorite sneakers to match. Enjoy your day!")
elif 70 <= temperature <= 85:
    print("It's getting pretty toasty out. Lets shed some layers. Grab a tank top, some shorts, and some sandals. Find some shade!")
elif temperature <= 85:
    print("It's HOT out!!!, wear light breathable fabrics, shorts or skirts, sunglasses, hats and sandals. Drink lots of water!") """  

""" #grading system  
grade_percentage = int(input("whats yout grade percentage?:"))
if 0<= grade_percentage <= 59:
    print("F for Fail")
elif 60<= grade_percentage <= 69:
    print("Below Average D")
elif 70<= grade_percentage <= 79:
    print("C's get degree's")
elif 80<= grade_percentage <= 89:
    print("B's are good")
elif 90<= grade_percentage <= 100:
    print("A's are Great")"""

"""#workout length advice
length_of_workout = int(input("How long have you been working out today?:"))
if 0<= length_of_workout <= 15:
    print("Its time to warm up,Dynamic stretches and light cardio should do you fine")
elif 15<= length_of_workout <= 30:
    print("Its time to start building the intensity, hop on the treadmill or start pumping iron")
elif 30<= length_of_workout <= 45:
    print("Its time to start building the core or strength train, planks or heavy squats or deadlifts")
elif 45<= length_of_workout <= 60:
    print("Its time to start cooling down. Stretch, foam roll, or rest")
else:
    print("Uh-oh!!! You either haven't started or your overtraining, Check your times")"""

"""#lets make coffe
sweetness_level = input("Choose your sweetness level(Type it in) Low, Medium, High: ").lower()
milk_level = input("Choose your milk level(Type it in) No milk, Some milk, Milk: "). lower()

if sweetness_level == "low" and milk_level == "no milk":
    print("Try a americano or a black coffee")
elif sweetness_level == "medium" and milk_level == "some milk":
    print("Try a Latte or a cafe au lait")
elif sweetness_level == "high" and milk_level == "milk":
    print("Try a Mocha or a Caramel Macchiato")
elif sweetness_level == "low" and milk_level == "some milk":
    print("Try a Cappuccino or a Flat White")
else:
    print("Maybe coffee's not what you are looking for... Check your inputs")"""

"""#library return
rental_length = int(input("How long have you had the book in days?: "))
fine = 0
if rental_length <= 5:
   fine = rental_length * 1
elif 6 <=  rental_length <= 10:
    fine = rental_length * 2
else:
    fine = rental_length * 5
print (fine)"""


