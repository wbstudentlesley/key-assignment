#carbon footprint quiz/game

#use a function to display separator at various locations
def separator():
	print("*" * 80)
	
#use a function for each question and checks for valid input
def get_input(prompt, valid_values):
    answer = input(prompt)
    #uses a while loop if the answer is invalid and needs to be asked again and converts the answer to lowercase
    while answer.lower() not in valid_values:
        print("That is not a valid option.  Please enter one of", valid_values)
        answer = input(prompt)
    return answer

separator()

print("Are you ready to lean about your carbon footprint?")
print("You will be asked a series of questions.")
print("Each answers will given a point value.")
print("Based on your answers you will recieve an estimate of your carbon footprint.")
print("This total is your carbon footprint measured in the number of pounds of carbon  \
dioxide created per year.\nThe lower the number, the fewer greenhouse gasses are emitted into the atmosphere.")

separator()

#ask the student for their name and print hello
name = input("What is your name? ")
print("Hello", name)
#sets the variable total_carbon_footprint to a starting value of 0
total_carbon_footprint = 0

separator()

#ask the student how they get to school
transportation = get_input("How do you get to school? (Enter 1 for walk, 2 for bike, 3 for car, 4 for bus, 5 carpool) ", ["1","2","3","4","5"])
if transportation == "1":
    print("Good job, you are reducing your carbon footprint and getting exercise.")
    #walking does not add to the carbon footprint so no calculation required on this line
elif transportation == "2":
    print("Good job, you are reducing your carbon footprint and getting exercise.")
    #biking does not add to the carbon footprint so no calculation required on this line
elif transportation == "3":
    print("Not great but maybe next time try carpooling or a bike, you have added 1115 to your carbon footprint.")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 1115
elif transportation == "4":
    print("Did you know buses do use a lot of gas.")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 131
elif transportation == "5":
    print("A carpool is better than a car on your own but it still adds 459 to your carbon footprint.")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 459
    
#ask the student what is the main type of food they eat
eat = get_input("Do you eat mostly - 1 meat, 2 vegetables, 3 bread?", ["1","2","3"])
if eat == "1":
    print("Did you know eating mean can add 644 to your carbon footprint. On average, beef and lamb production have the highest carbon footprints of all the foods. Find out more at https://sustainability.psu.edu/wp-content/uploads/2020/09/ReducingDiningReport.pdf")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 644 
elif eat == "2":
    print("Find out more about your carbon footprint and food https://www.greeneatz.com/foods-carbon-footprint.html")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 153
elif eat == "3":
    print("Find out more about your carbon footprint and food at https://www.greeneatz.com/foods-carbon-footprint.html")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 364

#ask the student if they turn off their lights 
lights = get_input("Do you turn off the lights when you leave the room? Enter y or n: ", ["y","n"])
if lights == "y":
    print("Good job, you are saving energy.")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 133
else:
    print("That's too bad try remembering to turn them off next time. ")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 268

#ask the student if they unplug appliances  
unplug = get_input("Do you unplug appliances/chargers when not in use? Enter y or n: ", ["y","n"])
if unplug == "y":
    print("Good job, you are saving energy.")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 9
else:
    print("That's too bad. The energy costs of plugged-in appliances can really add up, and unplugging these devices could save you up to $100 to $200 a year. https://blog.directenergy.com/should-you-unplug-appliances-when-not-in-use/. ")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 18
    
#ask the student how they dry their clothes
dryclothes = get_input("How do you dry clothes? (Enter 1 - hang to dry, 2 - dryer, 3 - both)", ["y","n"])
if dryclothes == "1":
    print("Good job, you are reducing your carbon footprint and getting exercise.")
    #does not add to the carbon footprint so no calculation required on this line
elif dryclothes == "2":
    print("Good job, you are reducing your carbon footprint and getting exercise.")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 750
elif dryclothes == "3":
    print("Not great but maybe next time try carpooling or a bike.")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 375

#ask the student if they leave the water running when brushing their teeth
teeth = get_input("Do you turn off the water when brushing your teeth. Enter y or n: ", ["y","n"])
if teeth == "y":
    print("Good job, you are saving energy.")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 34
else:
    print("That's too bad try remembering to turn them off next time. ")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 274

#ask the student if they leave the tv on    
tv = get_input("Do you turn off the TV when you’re not watching it?. Enter y or n: ", ["y","n"])
if tv == "y":
    print("Good job, you are saving energy.")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 47
else:
    print("That's too bad try remembering to turn them off next time. ")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint + 140

#ask the student if they recycle paper
recycle_paper = get_input("Do you recycle paper/magazines? Enter y or n: ", ["y","n"])
if recycle_paper == "y":
    print("Good job, you are reducing your carbon footprint.")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint - 105
else:
    print("That's too bad try recycling can reduce your carbon footprint by 105. ")

#ask the student if they recycle plastic
recycle_plastic = get_input("Do you recycle paper/magazines? Enter y or n: ", ["y","n"])
if recycle_plastic == "y":
    print("Good job, you are reducing your carbon footprint.")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint - 19
else:
    print("That's too bad try recycling can reduce your carbon footprint by 19. ")

#ask the student if they recycle glass    
recycle_paper = get_input("Do you recycle paper/magazines? Enter y or n: ", ["y","n"])
if recycle_paper == "y":
    print("Good job, you are reducing your carbon footprint.")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint - 7
else:
    print("That's too bad try recycling can reduce your carbon footprint by 7. ")


#ask the student if they recycle aluminum
recycle_aluminum = get_input("Do you recycle paper/magazines? Enter y or n: ", ["y","n"])
if recycle_aluminum == "y":
    print("Good job, you are reducing your carbon footprint.")
    #recalculates the total_carbon_footprint
    total_carbon_footprint = total_carbon_footprint - 86
else:
    print("That's too bad try recycling can reduce your carbon footprint by 86. ")
separator()

#prints the final value of the students total carbon footprint
print("Your total carbon footprint is", total_carbon_footprint)

print("What changes can you make in your life to reduce your carbon \
footprint? Try to make some of these changes in the next week and come back and play the game again.")

separator()


