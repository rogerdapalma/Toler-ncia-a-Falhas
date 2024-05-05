def exception_example():
    try:
        numbers = [1, 2, 3]
        print(numbers[3])  # This will raise an IndexError
    except IndexError as e:
        print("An error occurred:", e)
    else:
        print("No errors occurred.")
    finally:
        print("The 'try except' is finished.")

exception_example()
