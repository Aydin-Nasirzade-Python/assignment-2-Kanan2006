#import libraries here

def main():
  length = float(input("Enter the wavelength in nm: "))

  if length <= 750 and length >= 620:
     print("The relevant color is Red")
  elif length <= 750 and length >= 590:
     print("The relevant color is Orange")
  elif length <= 750 and length >= 570:
     print("The relevant color is Yellow")
  elif length <= 750 and length >= 495:
     print("The relevant color is Green")
  elif length <= 750 and length >= 450:
     print("The relevant color is Blue")
  elif length <= 750 and length >= 380:
     print("The relevant color is Violet")
  else:
     print("Invalid input!")
  pass
if __name__ == "__main__":
  main()
