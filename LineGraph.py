
################################################################################
# Author: Duong Dinh
# Date: April 18, 2021
# Description: Program to plot data and graph data 
################################################################################
import matplotlib.pyplot as plt

def main():
  listt = []
  xx = []
  # loop throguh to assigh stuff to if
  for i in range(1,53):
        xx.append(i)
  with open('filename.txt') as fo:
        for line in fo:
            # do what you gotta do to amke sure this and that
           line = line.replace("\n","")
           listt.append(float(line))

  fig, ax = plt.subplots()
  # plot the pue chart
  ax.set_title('title')
  # set stiff osd psf dsf sa fds
  ax.set_xlabel('x-axis')
  ax.set_ylabel('y-axis')

  ax.set_xlim(1,52)
  ax.set_ylim(1.5,4.25)
  ax.grid()
  ax.plot(xx, listt)
  plt.show()

if __name__ == '__main__':
    main()
    plt.show()
