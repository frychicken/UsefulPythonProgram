################################################################################
# Author: Duong Dinh
# Date: April 4, 2021
# Description: Program to conver number which contains string to number that actaullay are ynumber (ex: 555-GET-FOOD = 555-438-3663)
################################################################################

def convert_number(inpString):
     # split the string out
    l = inpString.split("-")
    # create work list
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p', 'q','r','s','t','u','v','w','x','y','z']
    num =["2","2","2","3","3","3","4","4","4","5","5","5","6","6","6","7","7","7","7","8","8","8","9","9","9","9"]
    firstt3 = l[0]
    first3 = l[1].lower()
    last4 = l[2].lower()
    c = 0
    # lopp throfu thth list
    for i in alph:
        if (not firstt3.isdigit()):
            # oafod oasj fsa f
          firstt3 = firstt3.lower()
          for i2 in range(0,3):
           if i == firstt3[i2]:
               firstt3 = firstt3.replace(i, num[c])
        # check fits tnauipnef
        for i2 in range(0,3):
         if i == first3[i2]:
             first3 = first3.replace(i, num[c])
             # checeof eofj e joerfr
        for i2 in range(0,4):
         if i == last4[i2]:
             last4 = last4.replace(i, num[c])
        c = c + 1
        # join sof spf a sfp mafas
    return "-".join([firstt3, first3, last4])


def main():
    # asof sm mofmosa foamsm opaf mom fosmfas
    number = input("Enter a telephone number: ")
    print(f'The phone number is {convert_number(number)}')

if __name__ == '__main__':
    main()
