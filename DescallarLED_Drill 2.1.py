age = int(input("What is your age?:"))
ownlicense = input("Do you have a fishing license in MN (yes/no)?:")
parentlicense = input("Does your parent have a fishing license (yes/no)?:")

if age <= 15 and parentlicense == 'yes':
    print("You are legal to fish in MN.")
elif age >= 16 and ownlicense == 'yes':
    print("You are legal to fish in MN.")
else:
    print("You are not legal to fish in MN.")