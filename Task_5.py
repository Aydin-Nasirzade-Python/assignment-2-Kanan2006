#import libraries here

def main():
ay=input("Enter a month [ex. March]: ")
  gun=int(input("Enter the day [ex. 12]: "))
  if (1<=gun<=31 and (ay=="December"or ay=="January" or ay=="March" or ay=="May" or ay=="July" or ay=="August" or ay=="October")) or (1<=gun<=30 and (ay=="April" or ay=="June" or ay=="September" or ay=="November")) or (1<=gun<=29 and ay=="February"):     
      if(ay=="December" and 22<=gun<=31) or (ay=="January" and 1<=gun<=19):
          print("Your zodiac sign is Capricorn")
      elif(ay=="January" and 20<=gun<=31) or (ay=="February" and 1<=gun<=18):
          print("Your zodiac sign is Aquarius")
      elif(ay=="February" and 19<=gun<=29) or (ay=="March" and 1<=gun<=20):
          print("Your zodiac sign is Pisces")
      elif(ay=="March" and 21<=gun<=31) or (ay=="April" and 1<=gun<=19):
          print("Your zodiac sign is Aries")
      elif(ay=="April" and 20<=gun<=30) or (ay=="May" and 1<=gun<=20):
          print("Your zodiac sign is Taurus")
      elif(ay=="May" and 21<=gun<=31) or (ay=="June" and 1<=gun<=20):
          print("Your zodiac sign is Gemini")
      elif(ay=="June" and 21<=gun<=30) or (ay=="July" and 1<=gun<=22):
          print("Your zodiac sign is Cancer")
      elif(ay=="July" and 23<=gun<=31) or (ay=="August" and 1<=gun<=22):
          print("Your zodiac sign is Leo")
      elif(ay=="August" and 23<=gun<=31) or (ay=="September" and 1<=gun<=22):
          print("Your zodiac sign is Virgo")
      elif(ay=="September" and 23<=gun<=30) or (ay=="October" and 1<=gun<=22):
          print("Your zodiac sign is Libra")
      elif(ay=="October" and 23<=gun<=31) or (ay=="November" and 1<=gun<=21):
          print("Your zodiac sign is Scorpion")
      elif(ay=="November" and 22<=gun<=30) or (ay=="December" and 1<=gun<=21):
          print("Your zodiac sign is Sagittarius")
  else:
      print("Either a month or a day is invalid!")
  pass

if __name__ == "__main__":
  main()
