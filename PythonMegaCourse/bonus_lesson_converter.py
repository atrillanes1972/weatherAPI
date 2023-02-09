feet_inches = input("Type height in feet and inches:")


def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.304 + inches * 0.0254
    return meters

result = (convert(feet_inches))

if result < 1:
    print(f"Kid cannot use the slide. His height is {result} meters.")
else:
    print(f"Kid can use the slide! his height is {result} meters.")