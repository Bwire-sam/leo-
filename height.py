#Ask for someone's height in centimeters and print their height converted to feet and inches.
import math
def main():
    height = float(input("Enter your height(cm): "))
    print(height_feet_Inches(height))


def height_feet_Inches(height):
    tall = height * 0.0328084
    feet = math.floor(tall)
    inches = round((tall- feet) * 12)
    if inches == 12:
        feet = feet + 1
        return f"Your height of {height} is {feet} feet long"
    else:
        return f"Your height of {height} is {feet} feet and {inches} inches long"

if __name__ == "__main__":
    main()
