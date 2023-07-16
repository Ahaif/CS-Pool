
- The code uses the argparse module to handle command-line arguments.
  - The options -h and --help display the help message when used.
  - The options -v and --version display the version of the program when used.
  - This functionality is implemented in the print_version() and print_help() functions.
    
- Reverse option:
  - The option -r or --reverse is used to reverse the infection.
  - The encryption key is provided as an argument to the -r option.
  - This functionality is implemented in the decrypt_files() function.
    
- Silent option:
  - The option -s or --silent is used to suppress any output during encryption/decryption.
  - This functionality is implemented by passing the silent argument to the encrypt_files() and decrypt_files() functions.

- Working directory and affected file extensions:
  - The code sets the INFECTION_FOLDER constant to the user's HOME directory followed by the "infection" folder.
  - The AFFECTED_EXTENSIONS constant contains the file extensions affected by Wannacry (e.g., .doc, .xls, .ppt).
  - The code filters files based on these affected extensions when encrypting or decrypting files.
    
- Encryption and renaming:
  - The code uses the cryptography library to perform encryption and decryption.
  - The encrypt_files() function encrypts the contents of the files in the specified folder using a provided key.
  - Files are renamed by adding the ".ft" extension using the ENCRYPTED_EXTENSION constant.
  - The code checks if a file already has the ".ft" extension and skips renaming it.
    
- Encryption key:
  - The code generates a key using the generate_key() function if the key file doesn't already exist.
  - The key is loaded from the key file using the load_key() function.
    
The choice of using the cryptography library for encryption is justified by its popularity, widespread usage, and reputation for providing secure encryption algorithms.
