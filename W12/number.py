def number():  # Question 1
    number_series = []
    while len(number_series) < 10:
        try:
            number_series.append(float(input("Enter a number: ")))
            print(
                f"Number of records to be stored in a list: {10 - len(number_series)}")
        except ValueError:
            print("Enter a number!")
    return f"Lowest number: {min(number_series)} | Highest number: {max(number_series)} | Number of numbers: {len(number_series)} | Average of the numbers: {sum(number_series)/len(number_series)}"

    print(number())
