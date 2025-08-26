def print_alternate_elements(input_list):
    """
    Prints alternate elements from a given list.
    """
    if not input_list:
        print("The list is empty.")
        return

    print("Alternate elements are:")
    # Using list slicing to get alternate elements (starting from index 0)
    for element in input_list[::2]:
        print(element)

def main():
    """
    Main function to get user input for a list and print alternate elements.
    """
    user_input = input("Enter elements of the list, separated by spaces: ")
    
    # Split the input string into a list of strings
    user_list = user_input.split()

    print_alternate_elements(user_list)

if __name__ == "__main__":
    main()
