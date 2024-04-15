age = int(input("Please enter your age:"))
citizen = input("Are you a natural born citizen of the U.S. (yes/no)?:")
years = int(input("How many years have you resided in the U.S.?:"))

candidate = True
if age >= 35 and citizen == 'yes' and years >= 14:
    candidate = True
if age < 35 or citizen == 'no' or years < 14:
    candidate = False
if candidate:
    print("You can run for president of USA")
else:
    print("You can't run for president of USA")