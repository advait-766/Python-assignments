def print_alternate_elements(input_list):
    if not input_list:
        print("The list is empty.")
        return

    print("Alternate elements are:")
    for element in input_list[::2]:
        print(element)

def main():
    user_input = input("Enter elements of the list, separated by spaces: ")
    user_list = user_input.split()
    print_alternate_elements(user_list)

if __name__ == "__main__":
    main()
