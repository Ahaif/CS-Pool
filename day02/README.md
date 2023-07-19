

- program that allows you to store an initial password in file, and that is capable of generating a new one time password
every time it is requested.
You can use any library that facilitates the implementation of the algorithm, as long
as it doesn’t do the dirty work, i.e. using a TOTP library is strictly prohibited. Of
course, you can and should use a library or function that allows you to access system
time.
• The executable must be named ft_otp
- program take arguments.
  - -g: The program receives as argument a hexadecimal key of at least 64 characters. The program stores this key safely in a file called ft_otp.key, which
is encrypted.
  - -k: The program generates a new temporary password based on the key given
as argument and prints it on the standard output.
  - program use the HOTP algorithm (RFC 4226).
  - The generated one-time password must be random and must always contain the
same format, i.e. 6 digits.
