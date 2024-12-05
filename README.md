# PassCrypV1
A simple script that hashed a password and then encrypts it with xor.
This script provides a basic example of a password encryption process using SHA-512 hashing and XOR encryption. The script takes a password as input, hashes it using SHA-512, encrypts the hashed password using XOR encryption, and outputs the encrypted password along with a welcome message.

## Usage

1. Run the script in an environment where it can accept user input (e.g., a terminal or an IDE that supports input/output).
2. Enter your desired password when prompted.
3. The script will hash your password using SHA-512, encrypt it using XOR encryption with a predefined key, and output the encrypted password along with a welcome message.
4. The script will then ask if you like the generated password and provide feedback based on your response.

## Script Details

- The `hash_password(password)` function takes a password as input and returns its SHA-512 hash.
- The `xor_encrypt(data, key)` function takes data and a key as input and encrypts the data using XOR encryption.
- The script prompts the user to enter their password and stores it in the `password` variable.
- The hashed password is then encrypted using XOR encryption with a predefined key (`key = b'mySecretKey'`).
- The encrypted password is then printed along with a welcome message.
- The script asks the user if they like the generated password and provides feedback based on their response.

## Security Considerations

Please note that this script is a simplified example and does not include proper security measures such as password salting, hashing iterations, or secure storage of sensitive data. In a production environment, you should consider using more robust and secure encryption mechanisms.

Also, the encryption key used in this script is a predefined byte string.
