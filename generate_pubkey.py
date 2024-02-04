import ecdsa

# Use secp256k1 curve
curve = ecdsa.SECP256k1

# Starting point (generator point)
generator_point = ecdsa.ecdsa.generator_secp256k1

# Number of public keys to generate
num_keys = 10

# Generate and print the public keys
for i in range(1, num_keys + 1):
    public_key = i * generator_point
    print(f"Public Key {i}: {public_key.x()}, {public_key.y()}")
