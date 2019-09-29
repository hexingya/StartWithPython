# if...else

# indentation is required to specify block
# age = 45
# if age == 45:
#     print("I'm {} year's old.".format(age))
# else:
#     print("I'm not {} year's old.".format(age))

# print("out of indentation...")

# odd even calc
# vehicle_number = input("Enter your vehicle number: ")

# if len(vehicle_number) == 4 and int(vehicle_number) != 0:
#     vehicle_number = int(vehicle_number)
#     if(vehicle_number % 2 == 0):
#         print("Even >> You can go")
#     else:
#         print("Odd >> You cannot go")
# else:
#     print("Invalid Vehicle Number")


fullmarks = 500
obtainedmarks = float(input("Enter obtained marks: "))

if(obtainedmarks >= 300):
    print("First Division")
elif(obtainedmarks < 300 and obtainedmarks >= 200):
    print("Second Divison")
elif(obtainedmarks < 200 and obtainedmarks >= 150):
    print("Third Division")
else:
    print("Fail...")
print("Thanks")
