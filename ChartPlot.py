
################################################################################
# Author: Duong Dinh
# Date: April 18, 2021
# Description: this is the program to plot data from txt
################################################################################
import matplotlib.pyplot as plt
import datetime
def main():
  list1 = []
  list2 = []
  # assign list and stuff
  last = 0.0
  with open('namefile.txt') as fo:
      for line in fo:
          strinng = line.split()
          # split, and substring do what i gotta do to make sute this and that
          list1.append(strinng[0])
          list2.append((last))
          # yest madkf asd fs fd dfs
          last = last + float(strinng[2])/1000

  fig, ax = plt.subplots()
       # plot the pue chart
  ax.set_title('Title')
       # set stiff osd psf dsf sa fds
  ax.set_xlabel('X-Axis Name')
  ax.set_ylabel('Y-Axis Name')
  #ax.set_yticklabels(['0', '100','200','300','400','500','600','700'])
  x = []
  for date in list1:
    y, m, d = date.split('-')
    # litesra fnjdsaf s fsa fs afds fds f
    dt = datetime.date(int(y), int(m), int(d))
    x.append(dt)
# ar ogd odsfjo dofsao djfosf jpa f

  ax.bar(x,list2,width = 1)
  fig.autofmt_xdate()
  plt.show()
if __name__ == '__main__':
    main()
    plt.show()
