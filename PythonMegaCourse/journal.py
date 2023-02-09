date = input("Today's date: ")
mood = input("How do you rate you mood today, from 1 to 10? ")
thoughts = input("Let your thoughts flow: ")

with open(date,'w') as file:
    file.write(f"The users mood level is {mood}!" + '\n' + '\n')
    file.write("Journal entry of the day: " + '\n' + f"{thoughts}")
