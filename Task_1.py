#import libraries here

def main():
  symbol = input("Enter a letter of the alphabet: ")

  if symbol == "a" or symbol == "e" or symbol == "i" or symbol == "o" or symbol == "u":
      print("Entered alphabet is a vowel!")
  elif symbol == "y":
      print("Sometimes it is a vowel, and sometimes it is a consonant!")
  else:
      print("Entered alphabet is a consonant!")
  pass
if __name__ == "__main__":
  main()
