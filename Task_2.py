#import libraries here

def main():
  month = input("Enter name of the month [ex. June]: ")

  day = int(input("Enter the day [ex. 5]: "))

  if month == "March" and day >= 20 or month == "April" or month == "May" or month == "June" and day <= 20:
      print(f"{month} {day} is in Spring")
  elif month == "June" and day >= 21 or month == "July" or month == "August" or month == "September" and day <= 21:
      print(f"{month} {day} is in Summer")
  elif month == "September" and day >= 22 or month == "October" or month == "November" or month == "December" and day <= 20:
      print(f"{month} {day} is in Fall")
  else:
      print(f"{month} {day} is in Winter")
  pass

if __name__ == "__main__":
  main()
