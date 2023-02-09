from bonus_lesson_converterfunctions import parse,convert

feet_inches = input("Type height in feet and inches:")

parsed = parse(feet_inches)

result = (convert(parsed['feet'],parsed['inches']))

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")

if result < 1:
    print(f"Kid cannot use the slide. His height is {result} meters.")
else:
    print(f"Kid can use the slide! his height is {result} meters.")