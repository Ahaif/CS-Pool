#!/usr/bin/env python3

import argparse
import hmac
import hashlib
from datetime import datetime
from cryptography.fernet import Fernet, base64

# Function to encrypt the key
def encrypt_key(key):
    f = Fernet.generate_key()
    fernet = Fernet(f)
    encrypted_key = fernet.encrypt(key.encode())
    return encrypted_key, f

# Function to decrypt the key
def decrypt_key(encrypted_key, f):
    fernet = Fernet(f)
    decrypted_key = fernet.decrypt(encrypted_key)
    return decrypted_key.decode()

# Function to generate the HOTP
def generate_hotp(key, counter, length=6):
    counter_bytes = counter.to_bytes(8, 'big')
    hmac_hash = hmac.new(key, counter_bytes, hashlib.sha1).digest()
    offset = hmac_hash[-1] & 0x0F
    truncated_hash = hmac_hash[offset:offset + 4]
    otp = int.from_bytes(truncated_hash, 'big') & 0x7FFFFFFF
    otp %= 10 ** length
    return str(otp).zfill(length)

# Function to validate the hexadecimal key
def validate_hex_key(key):
    try:
        bytes.fromhex(key)
        return True
    except ValueError:
        return False

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-g', dest='generate_key', metavar='KEY_FILE',
                       help='Generate and store an encrypted key')
    group.add_argument('-k', dest='generate_otp', metavar='KEY_FILE',
                       help='Generate and print a one-time password')
    args = parser.parse_args()

    if args.generate_key:
        with open(args.generate_key, 'r') as key_file:
            key = key_file.read().strip()

        if len(key) != 64 or not validate_hex_key(key):
            print('./ft_otp: error: key must be 64 hexadecimal characters.')
            return

        encrypted_key, f = encrypt_key(key)
        with open('ft_otp.key', 'wb') as otp_key_file:
            otp_key_file.write(encrypted_key)
        print('Key was successfully saved in ft_otp.key.')

    if args.generate_otp:
        with open(args.generate_otp, 'rb') as otp_key_file:
            encrypted_key = otp_key_file.read()

        with open('ft_otp.key', 'rb') as otp_key_file:
            encrypted_key = otp_key_file.read()

        decoded_key = base64.urlsafe_b64decode(encrypted_key)
        counter = int(datetime.now().timestamp()) // 30
        otp = generate_hotp(decoded_key, counter)
        print(otp)

if __name__ == '__main__':
    main()
