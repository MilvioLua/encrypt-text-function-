def encryption ( phrase):
    encrypt = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            encrypt = encrypt + "g"
        else:
            encrypt = encrypt + letter
    return encrypt

print(encryption(input("Enter a phrase")))

