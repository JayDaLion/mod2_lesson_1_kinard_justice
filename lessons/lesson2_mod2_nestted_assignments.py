"""#adventure game decisions

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?").lower()
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?").lower()
    if action == "light a torch":
        print("You can see clearer now, Proceed forward")
    elif action == "proceed in the dark":
        print("Good luck venturing in the dark")
else:
    pass"""

"""#event planner
attendees = int(input("Enter number of attendees: "))
is_veg = input ("Are you Vegan/Vegetarian? 'Yes' or 'No' ").lower()

if is_veg == "Yes": 
    answer = True
else:
    answer = False

venue = "large hall" if attendees > 100 else "conference room"
sound = "Audio System" if attendees > 300 else "Projector"
food = "Check out Veggie Delight Caterers" if is_veg == "yes" else "Check out Gourmet Meal Caterers"
print(venue, sound, food)"""