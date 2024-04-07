#import libraries here

def main():
  month = input("Enter a month [ex. March]: ")

  day = int(input("Enter the day [ex. 12]: "))

  if month == "December" and day >= 22 and day <= 31 or month == "January" and day <= 19 and day >= 1:
      print("Your zodiac sign is Capricorn")
  elif month == "January" and day >= 20 and day <= 31 or month == "February" and day <= 18 and day >= 1:
      print("Your zodiac sign is Aquarius")
  elif month == "February" and day >= 19 and day <= 29 or month == "March" and day <= 20 and day >= 1:
      print("Your zodiac sign is Pisces")
  elif month == "March" and day >= 21 and day <= 31 or month == "April" and day <= 19 and day >= 1:
      print("Your zodiac sign is Aries")
  elif month == "April" and day >= 20 and day <= 30 or month == "May" and day <= 20 and day >= 1:
      print("Your zodiac sign is Taurus")
  elif month == "May" and day >= 21 and day <= 31 or month == "June" and day <= 20 and day >= 1:
      print("Your zodiac sign is Gemini")
  elif month == "June" and day >= 21 and day <= 30 or month == "July" and day <= 22 and day >= 1:
      print("Your zodiac sign is Cancer")
  elif month == "July" and day >= 23 and day <= 31 or month == "August" and day <= 22 and day >= 1:
      print("Your zodiac sign is Leo")
  elif month == "August" and day >= 23 and day <= 31 or month == "September" and day <= 22 and day >= 1:
      print("Your zodiac sign is Virgo")
  elif month == "September" and day >= 23 and day <= 30 or month == "October" and day <= 22 and day >= 1:
      print("Your zodiac sign is Libra")
  elif month == "October" and day >= 23 and day <= 31 or month == "November" and day <= 21 and day >= 1:
      print("Your zodiac sign is Scorpion")
  elif month == "November" and day >= 22 and day <= 30 or month == "December" and day <= 21 and day >= 1:
      print("Your zodiac sign is Sagittarius")
  else:
      print("Either a month or a day is invalid!")
  pass

if __name__ == "__main__":
  main()
