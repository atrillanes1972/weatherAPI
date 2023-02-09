feet_inches = input("Type height in feet and inches:")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet,"inches": inches}


def convert(feet, inches):
    meters = feet * 0.304 + inches * 0.0254
    return meters

parsed = parse(feet_inches)

result = (convert(parsed['feet'],parsed['inches']))

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")

if result < 1:
    print(f"Kid cannot use the slide. His height is {result} meters.")
else:
    print(f"Kid can use the slide! his height is {result} meters.")