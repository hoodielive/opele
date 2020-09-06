import random
import string
import sys 

def generate_odu_characters():
    ''' 
    Function to generate all the 256 ascii characters that map to 
    Odu IFA. 
    '''

    return [chr(i) for i in range(256)]

def cast_Opele(number_of_times):
    '''
    Function to simulate the casting of the Opele Chain.
    The Function ttakes one parameter: number of times to
    throw the Opele chain.
    This generates random characters from the 256 Odu
    '''

    # Generate random Odu.
    
    secure_random = random.SystemRandom()
    odu_chars = generate_odu_characters()
    return  ''.join([secure_random.choice(odu_chars) for _ in range(number_of_times)])

def odu_cipher(message, secret_key):
    '''
    Function to either encrypt or decrypt a message with appropriate key.
    
    The function takes two parameters: 
    1. Message to encrypt or decrypt. 
    2. Secret key generated by the cast_Opele function.

    The function returns either an encrypted text or decrypted text depending on
    the message. It uses XOR encryption algorithm. This encryption is unbreakable
    if the key is larger than the message.
    '''

    # Ensure that the length of the key is the same as that of the message (pad it up with '0').

    encryption_key = secret_key.ljust(len(message), '0')

    # Ensure or Decrypt as appropriate with the given secret key using XOR.

    result = [chr (ord(a) ^ ord(b)) for a, b in zip(message, encryption_key)]
    return ''.join(result)

if __name__ == '__main__':
    print()

    message = input("Please enter message: ")
    print()

    binary_message = ''.join(['{0:08b}'.format(ord(m), 'b') for m in message])
    print()
    
    key_question = input('Do you want the system to generate random key for you? Y/N: ')
    print()

    key = ''
    if key_question.upper() == 'Y':
        key = cast_Opele(10)
    else:
        key = input('Please enter your secret key: ')

    if len(key.strip()) == 0:
        print('No secret key provided!')
        print('Exiting...')
        sys.exit(1)
    
    print('Secret key is: ' + repr(key))

    binary_key = ''.join(['{0:8b}'.format(ord(x), 'b') for x in key])
    print()

    print('Secret key in binary format: ', binary_key)
    print()

    encrypted_message = odu_cipher(message, key)
    print('Encrypted message is: ' + repr(encrypted_message))
    print()

    binary_encrypted_message = ''.join(['{0:08b}'.format(ord(e), 'b') for e in encrypted_message])
    print('Encrypted message in binary format is: ', binary_encrypted_message)

    print()
    print()
    print('Decrypting the message at the other end with the secret key..')
    print()

    decrypted_message = odu_cipher(encrypted_message, key)
    print('Decrypted message is: ', decrypted_message)

    print()

