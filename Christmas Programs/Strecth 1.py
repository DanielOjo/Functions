#Daniel Ogunlana
#Christmas Functions HW Task 1
#07/01/15


def getMode():
    while True:
        print("Do you want to encrypt or decrypt a message?")
        mode = input("Type e for encrypt or type d for decrypt: ")
        return mode
        
            
def getMessage():
    message = input("Please enter your message: ")
    return message

def getKey():
    print("Please enter the key number (1-25): ")
    key = int(input())
    return key
        

def getTranslatedMessage(mode, message, key):
    if mode[0] == "d":
        key = -key
    translated = ""
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    return translated

def mainProgram():
    mode = getMode()
    message = getMessage()
    key = getKey()
    print('Your translated text is:')
    print(getTranslatedMessage(mode, message, key))

mainProgram()
