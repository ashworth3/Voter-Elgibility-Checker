# Check user's voter elgibility on age input

# Collects user's age
age = int(input("How old are you? "))

#Checks if user is 18 or older, if so, they are elgible to vote
if age >= 18:
    print("Congratulations! You are eligible to vote. ✅")
else:
    print("Oops! You are not elgible to vote yet. ❌")
    print("You only have to wait " + str(18 - age,) + " years.")