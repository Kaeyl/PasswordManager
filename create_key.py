# -----------------------------------------------------------------------------------------------------------------------------------------
# This file was created by Kaylen Anderwald, 27/01/2023
# -----------------------------------------------------------------------------------------------------------------------------------------
from cryptography.fernet import Fernet

    # -----------------------------------------------------------------------------------------------------------------------------------------
    # The Create key class will generate a key for the specific file assigned. the key_type variable refers to the file. In the case of this
    # program key.key is the ket that encrypts the users stored passwords. The private.key refers to the single key that is used
    # to encrypt the users master password.
    # -----------------------------------------------------------------------------------------------------------------------------------------

class Create_key:
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # This function manages the key generation for both the key.key file and the private.key file
    # The key_type variable refers to the file. In the case of this program key.key is the ket that encrypts the users stored passwords.
    # The private.key refers to the single key that is used to encrypt the users master password
    # -----------------------------------------------------------------------------------------------------------------------------------------
    def write_key(key_type):
        key = Fernet.generate_key() # Generates the key
        with open(key_type, "wb") as key_file: # Opens the file the key is to be written to
            key_file.write(key) # Writes the key

    # -----------------------------------------------------------------------------------------------------------------------------------------
    # The encryption class is responsible for encrypting and decrypting the password files. This is done by using the existing keys generated
    # Create_key class.
    # -----------------------------------------------------------------------------------------------------------------------------------------
class Encryption:
    # -----------------------------------------------------------------------------------------------------------------------------------------
    # The encrypt function takes the text file i.e. user_passwords.txt and uses thee key.key file to encrypt the data so that it is unreadable.
    # The second variable "encryption_key" is the key file i.e. key.key or private.key. This allows the program to use the correct key for
    # the function. (THIS SECTION WILL BE AMENDED SHORTLY)
    # -----------------------------------------------------------------------------------------------------------------------------------------
    def encrypt(text, encryption_key):
        # using the key
        with open(encryption_key, 'rb') as filekey:
            key = filekey.read()
        # using the generated key
        fernet = Fernet(key)
        # opening the original file to encrypt
        with open(text, 'rb') as file:
            original = file.read()
        # encrypting the file
        encrypted = fernet.encrypt(original)
        # opening the file in write mode and
        # writing the encrypted data
        with open(text, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    # -----------------------------------------------------------------------------------------------------------------------------------------
    # The decrypt function takes the same variables as the above function, however, it reverses the encryption so that the user can read the
    # information. (THIS SECTION WILL BE AMENDED SHORTLY)
    # -----------------------------------------------------------------------------------------------------------------------------------------
    def decrypt(text, encryption_key):
        # using the key
        with open(encryption_key, 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        # opening the encrypted file
        with open(text, 'rb') as enc_file:
            encrypted = enc_file.read()
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
        # opening the file in write mode and
        # writing the decrypted data
        with open(text, 'wb') as dec_file:
            dec_file.write(decrypted)
