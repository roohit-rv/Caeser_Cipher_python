import art
print(art.logo)
def encrypt(text, shift):
    message=""
    for char in text:
        if char in alphabet:
            pos=alphabet.index(char)
            newpos=pos+shift
            message+=alphabet[newpos]
        else:
            message+=char
    print(message)
def decrypt(text, shift):
    message=""
    for char in text:
        if char in alphabet:
            pos=alphabet.index(char)
            newpos=pos-shift
            message+=alphabet[newpos]
        else:
            message+=char
    print(message)
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cont=True
while cont:
    print("Type encode to 'encrypt the message or type decode to 'decrypt' the message")
    code=input().lower()
    if code=="encode":
        text=input("enter the message ").lower()
        shift=int(input("enter the number of shift you want to perform "))
        shift=shift%25
        encrypt(text, shift)
    elif code=="decode":
        text=input("enter the message ").lower()
        shift=int(input("enter the number of shift you want to perform "))
        shift=shift%25
        decrypt(text, shift)
    else:
        print("enter the valid input")
    print("Type yes to continue or no to stop- ")
    res=input()
    if res=="no":
       cont=False
       print("goodbye")

