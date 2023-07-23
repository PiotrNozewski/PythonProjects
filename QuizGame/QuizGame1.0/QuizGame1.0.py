print("Welcome! Are You ready for a challenge?")

playing = input("Do you want to play? (Y/N): ").lower()
if playing == "y":
    print("Let's play then, brave champion!")
else:
    print("Do not play then, loser!")
    quit()

score = 0

answer = input("How much is 2 + 2? ")
if answer == "4":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("You got " + str(score) + " out of 4")

answer = input("What is the capital of Poland? ")
if answer == "Warsaw":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("You got " + str(score) + " out of 4")

answer = input("What is the capital of China? ")
if answer == "Beijing":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("You got " + str(score) + " out of 4")

answer = input("How much is 2 * 2 * 2? ")
if answer == "8":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("You've got " + str(score) + " out of 4")
print("Your performance is " + str((score/4) * 100) + "%")

if str(score) == "4":
    print("Congratulations! You are a champion of the arena! \nStorm, Earth and Fire! Heed my call!")
else:
    print("You need to practice more, weakling! ")

quit()
