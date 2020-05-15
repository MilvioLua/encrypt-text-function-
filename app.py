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

def descryption (descryptphrase):

    sword = 12
    sphrase = "milvio"
    descrypt = ""

    for letter in descryptphrase:
        if descryptphrase == sword:
            print(sphrase)
        else:
            print("worng enter again")

    return descrypt
print(descryption(input("Enter description")))