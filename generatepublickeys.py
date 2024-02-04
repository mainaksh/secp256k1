import ecdsa
from binascii import unhexlify

def find_target_key(initial_key, target_key, increment_value):
    # Convert target key to bytes
    target_key_bytes = unhexlify(target_key)

    # Initialize ecdsa curve
    curve = ecdsa.curves.SECP256k1.curve

    # Convert initial key to bytes
    initial_compressed_pub_key = unhexlify(initial_key)

    # Convert the compressed public key to a point
    initial_point = ecdsa.VerifyingKey.from_string(initial_compressed_pub_key, curve=ecdsa.SECP256k1).pubkey.point

    # Calculate the compressed public key corresponding to the increment value on the elliptic curve
    point_increment = ecdsa.ellipticcurve.Point(curve, int(ecdsa.curves.SECP256k1.generator.x()), int(ecdsa.curves.SECP256k1.generator.y()))
    point_increment *= increment_value

    # Perform the search
    count = 1
    target_found = False
    output_data = []

    while not target_found and count < 10000000:
        # Add the point representing the increment value to the current point
        new_point = initial_point + point_increment

        # Convert the new point back to a compressed public key
        compressed_pub_key = ecdsa.VerifyingKey.from_public_point(new_point, curve=ecdsa.SECP256k1).to_string('compressed')

        # Append the iteration and key to the output data
        output_data.append(f"Iteration {count + 1}: {compressed_pub_key.hex()}")

        # Check if the current public key matches the target key
        if compressed_pub_key == target_key_bytes:
            output_data.append(f"Target key found at iteration {count + 1}")
            target_found = True
            break

        count += 1
        initial_point = new_point  # Update the initial point with the new point

    if not target_found:
        output_data.append("Target key not found within the first 1 million iterations.")

    try:
        # Write output data to a file
        with open("1-100cr.txt", "w") as file:
            file.write("\n".join(output_data))
        print("Output file 'lst11.txt' created successfully.")
    except Exception as e:
        print(f"Error occurred while creating the output file: {str(e)}")

# Prompt user for initial key, target key, and increment value
initial_key = input("Enter the initial key in hex format: ").strip()
target_key = input("Enter the target key in hex format: ").strip()
increment_value = int(input("Enter the increment value: "))

# Call the function to find the target key
find_target_key(initial_key, target_key, increment_value)
