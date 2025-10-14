def main():
    time = str(input("What time is it: "))

    convert_time = convert(time)

    if 7.0 <= convert_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert_time <= 13.0:
        print("lunch time")
    elif 18.0 <= convert_time <= 19.0:
        print("dinner time")
    else:
        print("It's not meal time")


def convert(time):
    time = time.split(":")
    hours = int(time[0])
    minute = int(time[1])
    return hours + minute / 60


if __name__ == "__main__":
    main()