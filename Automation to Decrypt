import string

def create_caesar_matrix(shift):
    alphabet = string.ascii_letters + string.digits
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    caesar_dict = {orig: shifted for orig, shifted in zip(alphabet, shifted_alphabet)}
    return caesar_dict

def caesar_cipher(text, shift, direction='encrypt'):
    alphabet_length = len(string.ascii_letters + string.digits)
    caesar_dict = create_caesar_matrix(shift)
    result = []

    for char in text:
        if char in caesar_dict:
            encoded_num = (ord(caesar_dict[char]) - ord('A')) % alphabet_length
            result.append(encoded_num)
        else:
            encoded_num = ord(char) % alphabet_length
            result.append(encoded_num)

    return result

def caesar_decipher(encoded_message, shift):
    alphabet_length = len(string.ascii_letters + string.digits)
    caesar_dict = create_caesar_matrix(shift)
    reverse_caesar_dict = {shifted: orig for orig, shifted in caesar_dict.items()}

    # Get the characters for each encoded number
    decoded_chars = [reverse_caesar_dict.get((num - shift) % alphabet_length, chr((num - shift) % alphabet_length + ord('A'))) for num in encoded_message]

    # Convert the characters to a string, preserving only alphanumeric characters, spaces, and dots
    decoded_message = ''.join(char if char and char.isalnum() or char in ['.', ''] else ' ' if char == 'B' and decoded_chars[decoded_chars.index(char) - 1] == 'i' else '' for char in decoded_chars)

    return decoded_message

# Get user input for the encoded message and shift value
encoded_message = input("Enter the encoded message as a list of numbers, separated by spaces: ")
encoded_message = list(map(int, encoded_message.split()))

while True:
    try:
        shift = int(input("Enter the shift value used for encryption: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for the shift.")

# Decrypt the message
decoded_message = caesar_decipher(encoded_message, shift)

# Display the results
print("Decoded Message:", decoded_message)
