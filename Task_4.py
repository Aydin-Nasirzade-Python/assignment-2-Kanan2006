#import libraries here

def main():
   year = int(input("Enter the year [ex. 2021]: "))
    burcheyvani = ""
    if year % 12 == 0:
             burcheyvani = "Monkey"
    elif year % 12 == 1:
             burcheyvani = "Rooster"
    elif year % 12 == 2:
             burcheyvani = "Dog"
    elif year % 12 == 3:
             burcheyvani = "Pig"
    elif year % 12 == 4:
             burcheyvani = "Rat"
    elif year % 12 == 5:
             burcheyvani = "Ox"
    elif year % 12 == 6:
             burcheyvani = "Tiger"
    elif year % 12 == 7:
             burcheyvani = "Hare"
    elif year % 12 == 8:
             burcheyvani = "Dragon"
    elif year % 12 == 9:
             burcheyvani = "Snake"
    elif year % 12 == 10:
             burcheyvani = "Horse"
    elif year % 12 == 11:
             burcheyvani = "Sheep"
    if year >= 0:
        print("%d is the year of the %s" %(year, animal))
    else:
        print("Invalid year!")
  pass

if __name__ == "__main__":
  main()
