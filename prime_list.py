###################################################################################################
# Author: Duong Dinh
# Date: 03/2/2021
# Description: program to check if a given number is prime or not and give the list up to that number
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
 output =""
 num = int(input("Enter a positive integer: "))
 print(f'The primes up to {num} are: ', end='')
 for i in range (1, num+1):
   if is_prime(i):
    output = output + str(i) + ", "
 output = output[:-2]
 print(f'{output}')

   #call main
if __name__ == '__main__':
    main()
