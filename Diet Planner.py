def calculate_bmi(weight, height):
    # BMI = weight (kg) / (height (m))^2
    return weight / (height ** 2)

def recommend_meals(bmi):
    if bmi < 18.5:
        return ["High-calorie meals", "Protein-rich foods", "Nuts and dairy"]
    elif 18.5 <= bmi < 24.9:
        return ["Balanced diet with fruits and vegetables", "Lean proteins", "Whole grains"]
    elif 25 <= bmi < 29.9:
        return ["Low-carb meals", "Vegetables", "Lean protein"]
    else:
        return ["Low-calorie diet", "More fiber", "Avoid sugar and junk food"]

def main():
    print("=== Diet Planner ===")
    
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters (e.g., 1.75): "))
    lifestyle = input("Enter your lifestyle (Sedentary/Active/Very Active): ").lower()

    bmi = calculate_bmi(weight, height)
    print(f"\nHello {name}, your BMI is: {bmi:.2f}")

    meal_plan = recommend_meals(bmi)

    print("\nRecommended Meal Plan based on your BMI and Lifestyle:")
    for meal in meal_plan:
        print(f"- {meal}")

    if lifestyle == "sedentary":
        print("\nTip: Try to incorporate light exercises to improve health.")
    elif lifestyle == "active":
        print("\nGreat job staying active! Maintain balanced meals.")
    elif lifestyle == "very active":
        print("\nYou have a very active lifestyle. Ensure proper protein intake.")

if __name__ == "__main__":
    main()
