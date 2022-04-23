import os.path
import time

###########################

#Standard key alphabet to manage encryption and decryptions
key_alphabet = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g", "h": "h", "i": "i", "j": "j",
                "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "q", "r": "r", "s": "s", "t": "t",
                "u": "u", "v": "v", "w": "w", "x": "x", "y": "y", "z": "z"}

#Alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
new_alpha = ""


# Helper functions
# ==========================================#
def left(index):

    return alphabet[-index:] + alphabet[:-index]


def right(index):

    return alphabet[index:] + alphabet[:index]

#==============================================#
	

# ------Encoding algorithms------
	
def caesarShiftEncrypt(target_file1, choice):
    message = ""

    if choice == "encrypt":

        new_alpha= left(3)

        # Append new items to the alphabet list
        for i in range(len(key_alphabet)):
            key_alphabet[alphabet[i]] = new_alpha[i]

            # Perform file operation and read content to encrypt
        open_file = open(target_file1, "r")
        content = open_file.read()
        open_file.close()  # Save memory

        if content != "" or content is not None:

            for i in range(len(content)):

                if content[i] == " ":
                    #If there is a space
                    message += " "
                else:

                    message += str(key_alphabet.get(content[i]))



    elif choice == "decrypt":


        new_alpha = right(3)

        # Append new items to the alphabet list
        for i in range(len(key_alphabet)):
            key_alphabet[alphabet[i]] = new_alpha[i]

            # Perform file operation and read content to encrypt
            open_file = open(target_file1, "r")
            content = open_file.read()
            open_file.close()  # Save memory

        if content != "":

            for i in range(len(content)):

                if content[i] == " ":

                    message += " "
                else:

                    message += str(key_alphabet.get(content[i]))

    time.sleep(1)
    print("Encrypted message\n" + message)






def ROTShift(target_file2, choice , shift):
    message = ""

    if choice == "encrypt":


        new_alpha = left(shift)


        # Append new items to the alphabet list
        for i in range(len(key_alphabet)):
            key_alphabet[alphabet[i]] = new_alpha[i]

            # Perform file operation and read content to encrypt
        open_file = open(target_file2, "r")
        content = open_file.read()
        open_file.close()  # Save memory

        if content != "":

            for i in range(len(content)):

                if content[i] == " ":
                    # If there is a space
                    message += " "
                else:

                    message += str(key_alphabet.get(content[i]))




    elif choice == "decrypt":

        new_alpha = right(shift)

        # Append new items to the alphabet list
        for i in range(len(key_alphabet)):
            key_alphabet[alphabet[i]] = new_alpha[i]

            # Perform file operation and read content to encrypt
            open_file = open(target_file2, "r")
            content = open_file.read()
            open_file.close()  # Save memory

        if content != "":

            for i in range(len(content)):

                if content[i] == " ":

                    message += " "
                else:

                    message += str(key_alphabet.get(content[i]))



    time.sleep(1)
    print("Encrypted message\n" + message)




def vignereCypherShift(target_file_3 , choice , key):

        key_stream = ""#Repeated key
        letters = ""#final message

        #Read the content file
        open_file = open(target_file_3, "r")
        content = open_file.read()
        open_file.close()  # Save memory


        # Generate a the repeated key for encyrption
        for i in range(len(content)):
            key_stream += key[i % len(key)]




        if choice == "encrypt":

            for k in range(len(content)):
                #UNICODE character calculations after letter A-Z
                letters += chr(65 + ((ord(content[k]) + ord(key_stream[k])) % 26))##Start with the later A(formula for encryption of the sentence)



        elif choice == "decrypt":

            for k in range(len(content)):
                #UNICODE character calculation after letter A-Z
                letters += chr(65 + ((ord(content[k]) - ord(key_stream[k]))+ 26) % 26)#Decyption formula for decrypting the hidden sentence



        print("Decrypted message:" + letters)











# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print("------File encrypted and decrypted------")

    encrypt_decrypt = int(input("Would you like to encrypt or decrypt?\n1:Encrypt\n2:Decrypt\n"))

    if encrypt_decrypt == 1:

        file = input("Enter a file to encrypt\n")

        while not os.path.exists(file):
            print("File doesnt exist")
            time.sleep(1)
            file = input("Enter a file to encrypt\n")

        type = int(input("Encrypt with ROTx or Caesar shift?\n1:ROTX Encryption\n2:Caesar Encryption\n"))

        if type == 1:

            ROT_OPTION = int(input("Which ROT function would you like to implement\n1:ROT13\n2:Custom\n"))

            if ROT_OPTION == 1:

                ROTShift(file,"encrypt", 13)

            elif ROT_OPTION == 2:

                shift = int(input("Enter shift:\n"))

                ROTShift(file, "encrypt", shift)  # ROTX call tp encrypt


        elif type == 2:

            CAESAR_OPTION = int(input("Which Caesar shift would you like to perform?\n1:Normal Caesar\n2:Vignere "
                                      "Shift\n"))

            if CAESAR_OPTION == 1:

                caesarShiftEncrypt(file, "encrypt")



            elif CAESAR_OPTION == 2:

                key = str(input("Enter a key for the encryption\n"))

                vignereCypherShift(file, "encrypt", key)




    elif encrypt_decrypt == 2:

        file = input("Enter a file to decrypt\n")

        while not os.path.exists(file):
            print("File doesnt exist")
            time.sleep(1)
            file = input("Enter a file to decrypt\n")

        type = int(input("Encrypt with ROTx or Caesar shift?\n1:ROTX Decrypt\n2: Caesar Decrypt\n"))

        if type == 1:

            ROT_OPTION = int(input("Which ROT function would you like to implement\n1:ROT13\n2:Custom\n"))

            if ROT_OPTION == 1:

                ROTShift(file, "decrypt", 13)

            elif ROT_OPTION == 2:

                shift = int(input("Enter shift:\n"))

                ROTShift(file, "decrypt" , shift)  # ROTX call tp encrypt


        elif type == 2:

            CAESAR_OPTION = int(input("Which Caesar shift would you like to perform?\n1:Normal Caesar\n2:Vignere "
                                      "Shift\n"))

            if CAESAR_OPTION == 1:

                caesarShiftEncrypt(file, "encrypt")



            elif CAESAR_OPTION == 2:

                key = str(input("Enter a key for the encryption\n"))

                vignereCypherShift(file, "decrypt", key)


