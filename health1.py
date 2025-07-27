def calculate_bmi(weight, height_meters):
  return weight / (height_meters ** 2)
def prescribe_diet_plan(bmi, age):
  if bmi < 18.5:
  
    return "Underweight: Increase calorie intake and focus on protein and healthy fats."

  elif 18.5 <= bmi < 24.9:
    if age < 18:
      return "Normal weight: Focus on balanced nutrition for growth."
    else:
      return "Normal weight: Maintain a balanced diet with variety."
  elif 25 <= bmi < 29.9:
    return "Overweight: Reduce calorie intake, increase fruits, vegetables, and whole grains."
  else:
    return "Obesity: Significantly reduce calorie intake, consult a nutritionist."
def get_patient_info():
  name = input("Enter patient name: ")
  age = int(input("Enter patient age: "))
  weight = float(input("Enter weight in kg: "))
  height_meters = float(input("Enter height in meters: "))
  bmi = calculate_bmi(weight, height_meters)
  diet_plan = prescribe_diet_plan(bmi, age)
  print(f"\nPatient Name: {name}")
  print(f"Age: {age}")
  print(f"Weight: {weight} kg")
  print(f"Height: {height_meters} meters")
  print(f"BMI: {bmi:.2f}")
  print(f"Diet Plan: {diet_plan}")
def main():
  while True:
    print("\nHealth Management System")
    print("1. Enter Patient Information and Get Diet Plan")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
      get_patient_info()
    elif choice == '2':
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")
if __name__ == "__main__":
  main()

