months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def main():
    while True:
        try:
            month, day, year = input("Date: ").replace("/", " ").split(" ")
            if int(month) <= 12 and int(len(year)) == 4 and int(day) <= 31:
                print(f"{year}-{month}-{day}")
                break
        except ValueError:
                day = day.strip(",")
                if str(month.capitalize()) in months and int(len(year)) == 4 and int(day) <= 31:
                    print(f"{year}-{months[month.capitalize()]}-{day}")
                    break
        
main()