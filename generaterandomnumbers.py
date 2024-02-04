import random

# Generate a random 77-digit number
random_number = ''.join([str(random.randint(0, 9)) for _ in range(77)])

# Convert the random number to an integer
number = int(random_number)

# Define the modulus
modulus = 115792089237316195423570985008687907852837564279074904382605163141518161494337

# Open a file for writing
with open("or4.txt", "w") as file:
    # Write the original number to the file
    file.write(str(number) + "\n")

    # Perform operations to reduce the number to 20 digits
    iteration = 1
    while True:
        # Perform the operation (number * 10^77) % modulus
        number = (number * 10**77) % modulus
        # Write the result of the current iteration to the file
        file.write(str(number) + "\n")
        iteration += 1
        # Check for some external condition to break the loop (not based on the length of the number)
        # For instance, you could set a maximum number of iterations or use some other criteria
        if iteration > 1000000:  # For example, break after 1000 iterations
            break
