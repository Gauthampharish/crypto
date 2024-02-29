# import random
# import math

# def gcd(a, b):
#     """Euclid's Algorithm for GCD"""
#     while b != 0:
#         a, b = b, a % b
#     return a

# def multiplicative_inverse(e, phi):
#     """Extended Euclidean Algorithm"""
#     d = 0
#     x1, x2, y1, y2 = 0, 1, 1, 0
#     temp_phi = phi
    
#     while e > 0:
#         temp1 = temp_phi // e
#         temp2 = temp_phi - temp1 * e
#         temp_phi = e
#         e = temp2
        
#         x = x2 - temp1 * x1
#         y = y2 - temp1 * y1
        
#         x2 = x1
#         x1 = x
#         y2 = y1
#         y1 = y
    
#     if temp_phi == 1:
#         d = y2 + phi
    
#     return d

# def is_prime(num):
#     """Check if number is prime"""
#     if num <= 1:
#         return False
#     elif num <= 3:
#         return True
#     elif num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def generate_keypair(p, q):
#     """Generate public and private key pairs"""
#     if not (is_prime(p) and is_prime(q)):
#         raise ValueError("Both numbers must be prime.")
#     elif p == q:
#         raise ValueError("p and q cannot be equal")

#     n = p * q
#     phi = (p - 1) * (q - 1)

#     e = random.randrange(1, phi)

#     # Ensure e and phi are coprime
#     g = gcd(e, phi)
#     while g != 1:
#         e = random.randrange(1, phi)
#         g = gcd(e, phi)

#     d = multiplicative_inverse(e, phi)

#     # Return public and private key pair
#     # Public key is (e, n) and private key is (d, n)
#     return ((e, n), (d, n))

# def encrypt(public_key, plaintext):
#     """Encrypt the plaintext using public key"""
#     e, n = public_key
#     cipher = [(ord(char) ** e) % n for char in plaintext]
#     return cipher

# def decrypt(private_key, ciphertext):
#     """Decrypt the ciphertext using private key"""
#     d, n = private_key
#     plain = [chr((char ** d) % n) for char in ciphertext]
#     return ''.join(plain)



import random

# Euclid for divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclid for MI
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        x = x2 - temp1 * x1
        y = d - temp1 * y1
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    if temp_phi == 1:
        return d + phi

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True

def generate_prime():
    prime_candidate = 0
    while not is_prime(prime_candidate):
        prime_candidate = random.randint(100, 1000)  # Adjust the range as per your requirements
    return prime_candidate

def generate_key_pair():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))
def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), key, n) for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    aux = [str(pow(char, key, n)) for char in ciphertext]
    # Return the array of bytes as a string
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)

if __name__ == '__main__':
    public, private = generate_key_pair()
    print(" - Your public key is ", public, " and your private key is ", private)

    message = input(" - Enter a message to encrypt with your public key: ")
    encrypted_msg = encrypt(public, message)

    print(" - Your encrypted message is: ", ''.join(map(lambda x: str(x), encrypted_msg)))
    print(" - Decrypting message with private key ", private, " . . .")
    print(" - Your message is: ", decrypt(private, encrypted_msg))

