##################################Algorithm####################################################################
# 1. Define constants for punctuation and alphanumeric characters
# 2. Define a function print_banner that takes a message as input and displays it as a banner.
# 3. Define a function multiplicative_inverse that takes two integers A and M as input and returns the multiplicative inverse of A modulo M.
# 4. Define a function check_co_prime that takes two integers num and M as input and returns True if num and M are co-prime, otherwise returns False.
# 5. Define a function get_smallest_co_prime that finds the smallest coprime of a given number M.
# 6. Define a function caesar_cipher_encryption that encrypts a character using the Caesar Cipher.
# 7. Define a function caesar_cipher_decryption that decrypts a character using the Caesar Cipher.
# 8. Define a function affine_cipher_encryption that encrypts a character using the Affine Cipher.
# 9. Define a function affine_cipher_decryption that decrypts a character using the Affine Cipher.
# 10. Define a function main that takes a rotation N as input and asks the user to input a command (e)ncrypt, (d)ecrypt, (q)uit.
# 11. If the user inputs 'e', the program asks the user to input a string to encrypt.
# 12. If the user inputs 'd', the program asks the user to input a string to decrypt.
# 13. If the user inputs 'q', the program quits.
#multiplicative_inverse takes two integers A and M as input and returns the multiplicative inverse of A modulo M.

import math, string
PUNCTUATION = string.punctuation
ALPHA_NUM = string.ascii_lowercase + string.digits

BANNER = ''' Welcome to the world of 'dumbcrypt,' where cryptography meets comedy! 
    We're combining Affine Cipher with Caesar Cipher to create a code 
    so 'dumb,' it's brilliant. 
    Remember, in 'dumbcrypt,' spaces are as rare as a unicorn wearing a top hat! 
    Let's dive into this cryptographic comedy adventure!             
    '''

def print_banner(message):
    '''Display the message as a banner.
    It formats the message inside a border of asterisks, creating the banner effect.'''
    border = '*' * 50
    print(border)
    print(f'* {message} *')
    print(border)
    print()

def multiplicative_inverse(A, M):
    for x in range(M):
        if (A * x) % M == 1:
            return x

    '''Return the multiplicative inverse for A given M.
       Find it by trying possibilities until one is found.
        Args:
        A (int): The number for which the inverse is to be found.
        M (int): The modulo value.
        Returns:
            int: The multiplicative inverse of A modulo M.
    '''

def check_co_prime(num, M):
    '''
    check_co_prime takes two integers num and M as input and returns True if num and M are co-prime,
    otherwise returns False.
    '''
    if math.gcd(num, M) == 1 and num !=M:
        return True
    else:
        return False

def get_smallest_co_prime(M):
    '''
    #Define a function get_smallest_co_prime that finds the smallest coprime of a given number M.
    '''
    for i in range(2,M):
        if check_co_prime(i,M):
            return i
    return False

def caesar_cipher_encryption(ch,N,alphabet):
    '''
     Define a function caesar_cipher_encryption that encrypts a character using the Caesar Cipher.
    '''

    C = alphabet.index(ch)
    M = len(alphabet)
    ind =  (C+N)%M
    return  alphabet[ind]

def caesar_cipher_decryption(ch, N, alphabet):
    '''
     Define a function caesar_cipher_decryption that decrypts a character using the Caesar Cipher.
    '''
    C = alphabet.index(ch)
    M = len(alphabet)
    ind =  (C-N)%M
    return  alphabet[ind]

def affine_cipher_encryption(ch, N, alphabet):
    '''
    Define a function affine_cipher_encryption that encrypts a character using the Affine Cipher.
    '''
    C = alphabet.index(ch)
    M = len(alphabet)
    A = get_smallest_co_prime(M)
    ind =  ((A*C)+N)%M
    return  alphabet[ind]

def affine_cipher_decryption(ch, N, alphabet):
    '''
     Define a function affine_cipher_decryption that decrypts a character using the Affine Cipher.
    '''
    C = alphabet.index(ch)
    M = len(alphabet)
    A = get_smallest_co_prime(M)
    I = multiplicative_inverse(A, M)
    ind = (I*(C-N))%M
    return alphabet[ind]


def main():
    print_banner(BANNER)
    N = input("Input a rotation (int): ")
    while True:
        if N.isnumeric():
            N = int(N)
            break
        else:
            print("\nError; rotation must be an integer.")
            N = input("Input a rotation (int): ")
    while True:
        choice = input("\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ")
        if choice == 'e':
            st = input("\nInput a string to encrypt: ")
            st = st.lower()
            en = ''
            for i, ch in enumerate(st):
                if st[i].isalnum():
                    temp = affine_cipher_encryption(ch,N,ALPHA_NUM)

                elif ch in PUNCTUATION:
                    temp = caesar_cipher_encryption(ch, N, PUNCTUATION)
                    en = en+temp

                elif st[i].isspace()== True:
                    print("\nError with character:\n"
                          "Cannot encrypt this string.")
                    break
            if st[i].isspace() == False :
                print("\nPlain text:", st)
                print("\nCipher text:", en)
        elif choice == 'd':
            st = input("\nInput a string to decrypt: ")
            st = st.lower()
            de = ''
            for ch in st:
                if ch.isalnum():
                    temp = affine_cipher_decryption(ch,N,ALPHA_NUM)
                    de += temp
                elif ch in PUNCTUATION:
                    temp = caesar_cipher_decryption(ch, N,PUNCTUATION)
                    de += temp
                else:
                    a = 1
                    print("\nError with character:"
                          "Cannot encrypt this string.")
                    break

            print("\nCipher text:", st)
            print("\nPlain text:", de)
        elif choice == 'q':
            break
        else:
            print("\nCommand not recognized.")

if __name__ == '__main__':
    main()