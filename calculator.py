import streamlit as st
import json
import os

# JSON file to save calculations
json_file = 'calculations.json'

# Function to load calculations from JSON
def load_calculations():
    if os.path.exists(json_file):
        with open(json_file, 'r') as file:
            return json.load(file)
    return []

# Function to save a new calculation to JSON
def save_calculation(operation, result):
    calculations = load_calculations()
    calculations.append({"operation": operation, "result": result})
    with open(json_file, 'w') as file:
        json.dump(calculations, file)

# Main function for the Streamlit app
def main():
    st.title("Simple Calculator with History")
    
    # Input fields for numbers and operation
    num1 = st.number_input("Enter the first number:", value=0.0)
    operation = st.selectbox("Choose an operation:", ("+", "-", "*", "/"))
    num2 = st.number_input("Enter the second number:", value=0.0)
    
    # Perform calculation
    if st.button("Calculate"):
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Cannot divide by zero.")
                return
        
        # Display result
        st.write(f"Result: {result}")
        
        # Save the calculation
        save_calculation(f"{num1} {operation} {num2}", result)
    
    # Show previous calculations
    if st.button("Show Calculation History"):
        calculations = load_calculations()
        if calculations:
            st.subheader("Calculation History")
            for item in calculations:
                st.write(f"{item['operation']} = {item['result']}")
        else:
            st.write("No calculations found.")

if __name__ == "__main__":
    main()