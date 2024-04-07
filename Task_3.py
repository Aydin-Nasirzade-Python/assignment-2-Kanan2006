#import libraries here

def main():
  number=int(input("Enter the wavelength in nm: "))
  if 380<=number and number<=750:
    if 380<=number and number<450:
        print("The relevant color is Violet")
    elif 450<=number and number<495:
        print("The relevant color is Blue")
    elif 495<=number and number<570:
        print("The relevant color is Green")
    elif 570<=number and number<590:
        print("The relevant color is Yellow")
    elif 590<=number and number<620:
        print("The relevant color is Orange")
    else:
        print("The relevant color is Red")
  else:
    print("Invalid input!")

if __name__ == "__main__":
  main()
