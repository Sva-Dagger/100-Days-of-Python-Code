try:
    with open("open.txt") as file:
        New_file = file.read()
    a_dict = {"key":"value"}
    print(a_dict["key"])
except FileNotFoundError:
    with open("open.txt", "a") as file:
        file.write("something\n")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    print(New_file)
finally:
    file.close()
    print("File was closed")
