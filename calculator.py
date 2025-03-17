# Function to perform calculations
def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation."

#Main loop
def main():
    while True:
        try:
            #Ask the user for input
            num1=float(input("Enter the first number:"))
            num2=float(input("Enter the second number:"))
        except ValueError:
            print("Invalid input.Please enter valid numbers")
            continue
        operation=input("Enter the operation:(add,subtract,multiply,divide):")
        #Call the function and print the result
        result=calculate(num1,num2,operation)
        print(f"The result is:{result}")
        #Ask the user if they want to perform another calculation
        another=input("Do you want to perform another calculation?(yes/no):")
        if another.lower()!="yes":
            print("Goodbye!")
            break
#Run the main function
main()