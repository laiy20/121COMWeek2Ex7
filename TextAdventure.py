print("----------121COM Week 2 Lab Exercise 7----------") 
print("----------------<InsertTitleHere>---------------") 
print("---------------<InsertAuthorsHere>--------------") 
print("\n") 
 
 
print("You awake in a dark room.  Do you:") 
print("a) Scream for help.") 
print("b) Press the light switch") 
x = input("Enter a or b: ")
if x == "a": 
     print("Someone hears your screams...") 
     # Contine adventure Here
     print("You have two options now.")
    print("a) Leave the dark room.")
    print("b) Take a risk alone in this room and have an unforgettable experience")
    y = input("Enter a or b: ")
    if y == "a":
        print("Now you can see the sunshine and you are safe.")
    elif y == "b":
        print("You see a pretty witch standing in front of you")
        print("Faced with this situation, you can:")
        print("Chat with her throughout the night and listen to her special story a)")
        print("Walk towards her, give her a bear hug and keep on walking b)")
        print("Ignore her and take a risk here alone c)")
        z = input("Enter a , b or c: ")
        if z == "a":
            print("You had a great talk with the beautiful witch and knew more about her.After that, she places her magic 
            "stick in your pocket and promises she can help you to achieve three of your dreams.Eventually, she sends you out of
            "this dark room and you get an unforgettable experience")
        elif z == "b":
            print("Since you hugged the beautiful witch just now, you gained some luck from her.Therefore, though you walk
                  "alone now and almost scare to death for seeing lots of terrible stuff, you are relatively safe and find the
                  "exit eventually.You experienced a lot and become more courageous now")
        elif z == "c":
            print("Unfortunately, because you ignored the pretty witch just now, you were cursed by her and fell on evil days.
                  "Now, you are totally lost and it seems that you are walking in a huge maze.Though you find the exit eventually,
                  "you cannot open the door until you wait here alone for ten days")
        else
            print("That was not an option.  Game Over")
    else
        print("That was not an option.  Game Over")
elif x == "b": 
     print("The light comes on.") 
     print("You do not recognise the room but you have a really bad feeling...") 
     # Contine adventure Here 
else: 
     print("That was not an option.  Game Over") 
