def calculate_bmi():
    try:
        # Taking user input
        weight = float(input("Enter your weight (in kilograms): "))
        height = float(input("Enter your height (in meters): "))

        # Validate input
        if weight <= 0 or height <= 0:
            print("\n Weight and height must be positive numbers.")
            return

        # BMI Formula
        bmi = weight / (height ** 2)

        # Display BMI
        print("\nYour BMI is:", round(bmi, 2))

        # Categorize BMI
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal weight"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        print("BMI Category:", category)

    except ValueError:
        print("\nInvalid input! Please enter numeric values only.")


# Main Program Loop
print("WELCOME TO BMI CALCULATOR")

while True:
    calculate_bmi()

    choice = input("\nDo you want to calculate again? (yes/no): ").lower()
    if choice != "yes":
        print("\nThank you for using BMI Calculator")
        break
