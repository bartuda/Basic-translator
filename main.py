#source https://www.youtube.com/watch?v=z71azOGJQRo&list=PLLAZ4kZ9dFpMMs5lskzBApYXn0bl7emsW&index=25&ab_channel=MikeDane

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "X"
            else:
                translation = translation + "x"
        else:
            translation = translation + letter
    return translation
print((translate(input("Enter a phrase: "))))

#Another way
#def translate(phrase):
#    translation = ""
#    for letter in phrase:
#        if letter in "AEIOUaeiou":
#            translation = translation + "*"
#        else:
#            translation = translation + letter
#    return translation
#print((translate(input("Enter a phrase: "))))
