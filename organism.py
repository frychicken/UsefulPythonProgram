
# author: Duong Dinh
# Date: feb 17, 2021
# Description: Program to output that calulate organism
# about: Program to output organism population
#assign variables
startnum = int(input("Starting number, in million: "))
dayinc = int(input("Average daily increase, in percent: "))
daymultu = int(input("Number of days to multiply: "))

firr = startnum
# print first statement
print('Day   Approx. Pop')
print(f' {1:2d}      {startnum:8.4f}')
#start looping to see
for inn in range(1,daymultu):
    #done calculation and stuff
    print(f'{ inn+1:3d}      {(firr+firr*dayinc/100):8.4f}')
    firr = firr+firr*dayinc/100
