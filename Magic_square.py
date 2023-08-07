
################################################################################
# Author: DUONG Dinh
# Date: March 25, 2021
# Description: check magic square and print sqare for Lou SHu magic square
################################################################################

# Function printing the thing
def print_square(listt):

# loop throguh first
    string = ""
    for i in range(3):
        # loop throguh second
        for j in range(3):
            # print
            string = string + str(listt[i][j]) +" "

        print(f'{string.strip()}', end = '')
        string = ""
        print()

# chec kma gic
def is_magic(list):
    sum = 0
    sum2 = 0
    lis3 = []
    # assign variables
    lis4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
       for j in range(3):
           # loop thrnogu the things
        lis3.append(list[i][j])
    lis3.sort()
 # check if it contains all the number from 1 - 9
    if not (lis3 ==lis4):
       return False

# loop throfu check the sum if it is equal to 15
    for i in range(3):
        for j in range(3):
            sum+=list[i][j]
            sum2+=list[j][i]
        if not ((sum == 15) and (sum2 == 15)):
            return False
            # return false if it is not
        sum = 0
        sum2 = 0
        # adjacent from checke if sum is 15
    if not ((list[0][0] + list[1][1] + list[2][2] == 15) and (list[0][2] + list[1][1] + list[2][0] == 15)):
        return False

    return True

def main():

    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    m3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    # basically print out
    print("Your square is:")
    print_square(m1)
    if is_magic(m1):
        print("It is a Lo Shu magic square!")
    else:
        print("It is not a Lo Shu magic square.")
    print()
    print("Your square is:")
        # basically print out
    print_square(m2)
    if is_magic(m2):
            print("It is a Lo Shu magic square!")
    else:
            print("It is not a Lo Shu magic square.")
    print()
    print("Your square is:")
        # basically print out
    print_square(m3)
    if is_magic(m3):
            print("It is a Lo Shu magic square!")
    else:
            print("It is not a Lo Shu magic square.")

if __name__ == '__main__':
    main()
