#Daniel
#Stretch exercise task 1
#06/01/15

def user_information():
    message= input("Please enter your message: ")
    question= int(input("Please enter a shift value: "))
    return message, question

def encrypting(message, question):
    encrypted_message = ""
    for character in message:
        encrypt = ord(character)
        encrypt = encrypt + question
        encrypt_2 = chr(encrypt)
        encrypted_message = encrypted_message + encrypt_2
    return encrypted_message
    

def decrypting(message, question):
    question = -question
    decrypted_message = ""
    for character in message:
        decrypt = ord(character)
        decrypt = decrypt + question
        decrypt_2 = chr(decrypt)
        decrypted_message = decrypted_message + decrypt_2
    return decrypted_message
        
def display(decrypted_message):
    print(decrypted_message)

def display(encrypted_message):
    print(encrypted_message)

def main_program(): 
    message, question = user_information()
    answer = False
    while answer == False:
        print("Do you want to encrypt or decrypt a message?")
        choice = input("Type E to encrypt or D to decrypt a message: ")
        choice = choice.upper()
        choice = choice[0]
        if choice == "E":
            encrypt = encrypting(message, question)
            display(encrypt)
            answer = True
        elif choice == "D":
            decrypt= decrypting(message, question)
            display(decrypt)
            answer = True
        else:
            print("Please type in E or D")


main_program()

     
   
    
    

        
