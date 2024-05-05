def read_process_file():
    try:
        with open("example.txt", "r") as file:
            data = file.read()
            print(data)
        raise ValueError("Simulated Error")  # Simula um erro após a leitura
    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("An error occurred while reading or writing to the file.")
    except Exception as e:
        print("A general error occurred:", e)
    finally:
        print("Execution completed, whether an error occurred or not.")

read_process_file()
