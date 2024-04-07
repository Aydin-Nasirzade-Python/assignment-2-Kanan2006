#import libraries here

def main():
  letter = input(" Enter a letter of the alphabet: ")
  if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("Entered alphabet is a vowel!")
  elif letter == "y":
    print("Sometimes it is a vowel, and sometimes it is a consonant!")
  else:
    print("Entered alphabet is a consonant!")
  pass

if __name__ == "__main__":
  main()
