################################################################################
# Author: DUong Dinh
# Date: April 4, 2021
# Description: program to generate file statistic how many words and lines
################################################################################

def main():
  everything = ""
  c = 0
  # count how many words in the file
  with open('rumpelstiltskin.txt') as fo:
      everything = fo.read()

  l = everything.split()
  # count how many lunes in  a file
  with open('rumpelstiltskin.txt') as fo:
      for line in fo:
          c = c + 1

  # print out total worjs and line
  print(f'Total number of words: {len(l)}')
  print(f'Total number of lines: {c}')
  print(f'Average number of words per line: {len(l)/c:.1f}')

if __name__ == '__main__':
    main()
