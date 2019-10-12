import random

#A subroutine to replace all "-" (empty characters) with a random letter
def randomFill(wordsearch, size):
  LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for row in range(0,size):
    for col in range(0,size):
      if wordsearch[row][col]=="-":
        randomLetter = random.choice(LETTERS)
        wordsearch[row][col]=randomLetter

#Create an empty size by size wordsearch (list of lists)
def createWordsearch(size):
  wordsearch = []
  for row in range(0, size):
    wordsearch.append([])
    for col in range(0, size):
      wordsearch[row].append("-")
  return wordsearch

#A subroutine to output the wordsearch on screen
def displayWordsearch(size, wordlist):
  wordsearch = createWordsearch(size)
  for word in wordlist:
    word = "".join(word.upper().split(" "))
    addWord(word, wordsearch, size)
  randomFill(wordsearch, size)
  top_bottom_border = '_'
  print(' ' + top_bottom_border * ((size * 2) + 1) + ' ')
  space_var = ' '
  print('| ' + space_var * size * 2 + '|')
  for row in range(0,size):
    line="| "
    for col in range(0,size):
      line = line + wordsearch[row][col] + " "
    line = line + "|"
    print(line)
  print(' ' + top_bottom_border * ((size * 2) + 1) + ' ')

#A subroutine to add a word to the wordsearch at a random position
def addWord(word, wordsearch, size):
  row=random.randint(0,(size-1))
  col=0
  for i in range(0,len(word)):
    wordsearch[row][col+i]=word[i]
