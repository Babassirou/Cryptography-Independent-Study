# Initialize variables
p = 0
q = 0
cipher = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ."
public_key = 0
secret_key = 0
plain_text = ""
encrypted_text = ""
key_words = ""
key_numbers = ""
run = True

# Main loop
while run:
    # User input for two prime numbers, p and q
    p, q = input("Enter two key numbers separated by space; they should be prime numbers: \n #").split(" ")
    p = int(p)
    q = int(q)

    # Calculate modulus (n) and totient (z)
    n = p * q
    z = (p - 1) * (q - 1)

    # Find a suitable public key
    for i in range(2, 10000):
        if z % i != 0:
            public_key = round(i)
            break

    # Find the corresponding secret key
    for j in range(1, 10000):
        d = 1 + (j * z)
        d2 = d / public_key
        if d2.is_integer():
            secret_key = round(d2)
            break

    # Inner loop for user interaction
    start = True
    while start:
        # Display key information and available commands
        print("p = ", p)
        print("q = ", q)
        print("modulo = ", n)
        print("public_key ", public_key)
        print("secret_key = ", secret_key)
        print("COMMANDS")
        print("-en encrypt plain text")
        print("-de decrypt encrypted text")
        print("-exit exit the program")

        # User command input
        word = input("#")

        # Check user commands
        if "-exit" in word:
            run = False
            start = False
        elif "-en" in word:
            # Encryption: User inputs plain text, and the code converts it to encrypted text
            plain_text = input("Enter plain text: ")
            encrypted_text = " ".join([str((ord(char) ** public_key) % n) for char in plain_text])
            print("Encrypted text:", encrypted_text)
            input("Press Enter")
        elif "-de" in word:
            # Decryption: User inputs encrypted text, and the code converts it back to plain text
            encrypted_text = input("Enter encrypted text: ")
            decrypted_text = "".join([chr((int(s) ** secret_key) % n) for s in encrypted_text.split(" ") if s])
            print("Decrypted text:", decrypted_text)
            input("Press Enter")
