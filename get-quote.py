import random
import itertools

def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 16
  quote_rnd = random.randint(0, last-1)
  for _ in itertools.repeat(None, quote_rnd):
    rnd = random.randint(0, last)
    print(quotes[rnd], end='')

  rnd = random.randint(0, last)
  print(quotes[rnd], end='')

if __name__== "__main__":
  primary()
