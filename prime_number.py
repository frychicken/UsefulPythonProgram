###################################################################################################
# Author: Duong Dinh
# Date: 03/2/2021
# Description: program to check if a given number is prime or not
# About: program to check if a given number is prime or not
# program to check if a given number is prime or not
###################################################################################################
import math
#check if it is a prime number
def is_prime(num):
  if num == 1:
     return False
     # loop through the number to check if there is any
  for i in range (2, int(math.sqrt(num)) +1 ):
      # if it is
   if num % i == 0:
    return False
    # return true if it is
  return True

# main function
def main():
    # get input
 num = 0
 while num !=-1:
  num = int(input("Enter a positive integer (-1 to quit): "))
  if not num == -1:
  # print out of the check prime
   if is_prime(num):
    print(f'{num} is a prime number.')
   else:
      # if not
    print(f'{num} is not a prime number.')

   #call main
if __name__ == '__main__':
    main()
