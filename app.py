def encryption (phrase):
    encrypt = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            encrypt = encrypt + "g"
        elif letter in "ml":
            encrypt = encrypt + "6"

        else:
            encrypt = encrypt + letter
    return encrypt

print(encryption(input("Enter a phrase")))

unccrypt = ""
uword = "milvio"
upass = 12

def unccryption (phrase):
    if phrase == "12":
        print(uword)
    else:
        print("wrong password try again")
    return unccrypt

print(unccryption(input("enter password")))