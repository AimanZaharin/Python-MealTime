
def main():

    time = input("What time is it? ")
    newTime = convert(time)

    if 7 <= newTime <= 8:
        print("breakfast time")
    elif 12 <= newTime <= 13:
        print("lunch time")
    elif 18 <= newTime <= 19:
        print("dinner time")
    else:
        print("snack time")

def convert(time):

    newTime = time.replace(":",".")
    hours, sep, mins = newTime.partition(".")

    hours = float(hours)
    mins = float(mins)

    conmins = mins/60

    total = hours + conmins

    return total

main()

#split, which separates a str into a sequence of values, 
#all of which can be assigned to variables at once. 
#For instance, if time is a str like "7:30", then

#hours, minutes = time.split(":")

#will assign "7" to hours and "30" to minutes.