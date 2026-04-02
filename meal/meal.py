def main():
    give_me_the_time = input("What time is it? ")
    finished_converted = convert(give_me_the_time)

    if 7 <= finished_converted <= 8:
        print("breakfast time")
    elif 12 <= finished_converted <= 13:
        print("lunch time")
    elif 18 <= finished_converted <= 19:
        print("dinner time")


def convert(time="0:00"):
    hour, minut = time.split(":")
    return int(hour) + int(minut) / 60


if __name__ == "__main__":
    main()
