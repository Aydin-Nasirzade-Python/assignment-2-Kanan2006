#import libraries here

def main():
  year = int(input("Enter the year [ex. 2021]: "))

  if year < 0:
      print("Invalid year!")
  else:
      if (year - 2000) % 12 == 0:
          print(f"{year} is the year of the Dragon")
      elif (year - 2000) % 12 == 1:
          print(f"{year} is the year of the Snake")
      elif (year - 2000) % 12 == 2:
          print(f"{year} is the year of the Horse")
      elif (year - 2000) % 12 == 3:
          print(f"{year} is the year of the Sheep")
      elif (year - 2000) % 12 == 4:
          print(f"{year} is the year of the Monkey")
      elif (year - 2000) % 12 == 5:
          print(f"{year} is the year of the Rooster")
      elif (year - 2000) % 12 == 6:
          print(f"{year} is the year of the Dog")
      elif (year - 2000) % 12 == 7:
          print(f"{year} is the year of the Pig")
      elif (year - 2000) % 12 == 8:
          print(f"{year} is the year of the Rat")
      elif (year - 2000) % 12 == 9:
          print(f"{year} is the year of the Ox")
      elif (year - 2000) % 12 == 10:
          print(f"{year} is the year of the Tiger")
      else:
          print(f"{year} is the year of the Hare")
  pass

if __name__ == "__main__":
  main()
