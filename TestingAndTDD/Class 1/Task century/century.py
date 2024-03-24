def get_century(year):
    if year < 1:
        return "Nice! You are not even in the first century yet!"
    else:
        return ((year - 1) // 100) + 1


if __name__ == "__main__":
    year = int(input("Enter the Year: "))
    result = get_century(year)
    print(result)
