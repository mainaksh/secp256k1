from sympy import Mod

def main():
    modulus = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    while True:
        try:
            command = input("command: ").strip()
            if not command:
                raise ValueError("Empty input")

            # Split the command into tokens using whitespace as a separator
            tokens = command.split()

            # Ensure that the command has the correct number of tokens
            if len(tokens) != 3:
                raise ValueError("Invalid command format. Please ensure the format is '<num1> <operator> <num2>'.")

            # Extract tokens
            expression, operator, num2 = tokens

            # Ensure the operator is valid
            if operator not in ('+', '-', 'x', '/'):
                raise ValueError("Invalid operator. Please use '+', '-', 'x', or '/'.")

            # Extract num1 from the expression
            num1 = int(expression)

            # Ensure num2 is a valid integer
            num2 = int(num2)

            # Perform the operation based on the operator
            if operator == '+':
                result = Mod(num1 + num2, modulus)
            elif operator == '-':
                result = Mod(num1 - num2, modulus)
            elif operator == 'x':
                result = Mod(num1 * num2, modulus)
            elif operator == '/':
                result = Mod(num1 * pow(num2, -1, modulus), modulus)  # Modular multiplicative inverse

            print(f"Result: {result}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
