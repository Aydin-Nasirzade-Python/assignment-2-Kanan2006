#import libraries here

def main():
  month = input("Enter name of the month [ex. June]: ")
  day = int(input("Enter the day [ex. 5] : "))
  if month == "March" and (day>=20 and  day<=31) or month == "April" and day>=1 and day<=31 or month=="May" and day>=1 and day<=31 or (month=="June" and (day>=1 and day<21)):
    print(f"{month} {day} is in Spring")
  elif month == "June" and (day>=21 and day<=30) or month=="July" and day>=1 and day<=31 or month=="August" and day>=1 and day<=31 or (month=="September" and (day>=1 and day<22)):
    print(f"{month} {day} is in Summer")
  elif month=="September" and (day>=22 and day<=31) or month=="October" and day>=1 and day<=31 or month=="November" and day>=1 and day<=31 or month=="December" and day>=1 and day<21:
    print(f"{month} {day} is in Fall")
  else:
    print(f"{month} {day} is in Winter")
  pass

if __name__ == "__main__":
  main()
