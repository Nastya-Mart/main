from fake_math import divide as fake_divide
from true_math import divide as true_divide

def main():
    first_number = 10
    second_number = 0

    fake_result = fake_divide(first_number, second_number)
    true_result = true_divide(first_number, second_number)

    print("Результат fake_math.divide:", fake_result)
    print("Результат true_math.divide:", true_result)


if __name__ == "__main__":
    main()