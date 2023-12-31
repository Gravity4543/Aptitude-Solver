import random

def generatePassword(pwlength):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    password = "" 
    for j in range(pwlength):
        next_letter_index = random.randrange(len(alphabet))
        password = password + alphabet[next_letter_index]
        
    password = replaceWithNumber(password)
    password = replaceWithUppercaseLetter(password)
        
    
    
    return password


def replaceWithNumber(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        return pword


def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
        return pword



def main():

    lengths=6
    
    Password = generatePassword(lengths)
    print(Password)

    



main()