#Ask for someone's height in centimeters and print their height converted to feet and inches.
import math
def main():
    height = float(input("Enter your height(cm): "))
    print(height_feet_Inches(height))


def height_feet_Inches(height):
    tall = height * 0.0328084
    inches = round((tall- math.floor(tall)) * 12)
    return f"Your height of {height} is {math.floor(tall)} feet and {inches} inches long"

if __name__ == "__main__":
    main()
