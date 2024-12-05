import hashlib


def hash_password(password):
    """
    Hashes a password using SHA-512 algorithm.
    :param password: The password to be hashed.
    :return: The hashed password.
    """
    hashed_password = hashlib.sha512(password.encode()).hexdigest()
    return hashed_password


def xor_encrypt(data, key):

#Encrypts data using XOR encryption.

    encrypted_data = bytearray(len(data))
    for i in range(len(data)):
        encrypted_data[i] = data[i] ^ key[i % len(key)]
    return encrypted_data


# Get user input for the password
password = input("Enter your password: ")

# Hash the password
hashed_password = hash_password(password)

# Encrypt the hashed password using XOR encryption
key = b'mySecretKey'
encrypted_password = xor_encrypt(hashed_password.encode(), key)

# Output the encrypted password.
print("Here is your new and safe password, you are welcome king!")
print("Encrypted password:", encrypted_password.hex())

like = input("\ndo you like it?")
does_he = "yes"
nope = "no"

if like == does_he:
    print("nice:)")
elif like == nope:
    print("too bad, try another password")
    print("too bad, try another password")
input("\nPress Enter to exit...")
