import random
import string

def generate_vigenere_key(length=8):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

if __name__ == "__main__":
    key_length = int(input("Enter key length for testing key generation: "))
    key = generate_vigenere_key(key_length)
    print("Generated Key:", key)