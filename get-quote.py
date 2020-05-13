import random
def prime():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  ind = random.randint(0, last)
  print(quotes[ind])

if __name__== "__main__":
  prime()
