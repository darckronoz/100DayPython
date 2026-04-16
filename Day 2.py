#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha

#Tip Calculator
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_quantity = int(input("How many people to split the bill? "))
amount_per_person = (total_bill+(total_bill*tip_percentage/100))/people_quantity
print(f"Each person should pay: ${amount_per_person:.2f}")
#to round a number on a F-String we can use this way
#the other way would be to use the round() built in function.