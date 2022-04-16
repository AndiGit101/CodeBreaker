'''
This project is the codebreaker encrypted and decrypter for content written in py.
Functions use ceaser shift and reverse ceaser algorithm
'''

import fileinput
import os.path
import math
import time

############################


# Encoding algorithms
def caesarShiftEncrypt(target_file1 , choice):
	
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_message = ""
	
    key_alphabet = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g",  "h":"h", "i": "i", "j": "j", "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "q", "r": "r", "s": "s", "t": "t", "u": "u", "v": "v", "w": "w", "x": "x", "y": "y", "z": "z"}
	
	    
		
    if choice == "encrypt":
	
		
	    modified_alphabet = alphabet[-3:] + alphabet[:-3]  # Shift right 3
	
	    # Append new items to the alphabet list
	    for i in range(len(key_alphabet)):
	        key_alphabet[alphabet[i]] = modified_alphabet[i]
	
	
	    #Perform file operation and read content to encrypt
	    open_file = open(target_file1, "r")
	    content = open_file.read()
	    open_file.close()#Save memory
	
	
	    if content != "" or content is not None:
	
	        for i in range(len(content)):
	
	            if content[i] == " ":
	
	                encrypted_message += " "
	            else:
	
	                encrypted_message += str(key_alphabet.get(content[i]))
	
	    print("Encrypted message\n" + encrypted_message)
	

    elif choice == "decrypt":

		 
	      for i in range(3):
	
		      #left
		      for i in range(len(alphabet) -1):
		
		        temp = alphabet[i+1]
		        alphabet[i+1] = alphabet[i]
		        alphabet[i] = temp


			 # Append new items to the alphabet list
    for i in range(len(key_alphabet)):
				   
            key_alphabet[alphabet[i]] = modified_alphabet[i]

	
    if content != "" or content is not None:
	
	        for i in range(len(content)):
	
	            if content[i] == " ":
	
	                encrypted_message += " "
	            else:
	
	                encrypted_message += str(key_alphabet.get(content[i]))


	
    
	  print("Encrypted message\n" + encrypted_message)
	
      



def ROTShift(target_file2, index2):
    print("File could not be decrypted. File not found")

    key_alphabet = {"a": "a", "b": "b", "c": "c", "d": "d", "e": "e", "f": "f", "g": "g",
                    "h": "h", "i": "i", "j": "j", "k": "k", "l": "l", "m": "m", "n": "n", "o": "o", "p": "p", "q": "q",
                    "r": "r", "s": "s", "t": "t", "u": "u", "v": "v", "w": "w", "x": "x", "y": "y", "z": "z"}

    alphabet = "abcdefghijklmnopqrstuvwxyz"





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

            ROT_OPTION = int(input("Which ROT function would you like to implement\n1:ROT132:Custom\n"))

            if ROT_OPTION == 1:

                ROTShift(file, 13)

            elif ROT_OPTION == 2:

                shift = int(input("Enter shift:\n"))

                ROTShift(file, shift)  # ROTX call tp encrypt


        elif type == 2:

            caesarShiftEncrypt(file , "encrypt")





    elif encrypt_decrypt == 2:

        file = input("Enter a file to decrypt\n")

        while not os.path.exists(file):
            print("File doesnt exist")
            time.sleep(1)
            file = input("Enter a file to decrypt\n")

        type = int(input("Encrypt with ROTx or Caesar shift?\n1:ROTX Decrypt\n2: Caesar Decrypt"))

        if type == 1:

            ROT_OPTION = int(input("Which ROT function would you like to implement\n1:ROT132:Custom"))

            if ROT_OPTION == 1:

                ROTShift(file, 13)

            elif ROT_OPTION == 2:

                shift = int(input("Enter shift:\n"))

                ROTShift(file, shift)  # ROTX call tp encrypt


        elif type == 2:

            caesarShiftEncrypt(file , "decrypt")
