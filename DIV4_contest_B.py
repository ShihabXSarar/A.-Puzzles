def print_matrix(input_number):
    row=[]
    pr = ["##", "##"]
    dot = ["..", ".."]
    for i in range(1, input_number+1):
        for j in range(1, input_number+1):
            if (i % 2 != 0 and j % 2 != 0) or (i % 2 == 0 and j % 2 == 0):
                for element in pr:
                    row.append(element)
                    print(element, end="")
                print(end="")  # This line is not necessary

            else:
                for g in dot:
                    print(g, end="")
        print()  # Move this print statement outside the inner loop

if __name__ == "__main__":
    try:
        input_num = int(input("Enter a number: "))
        if input_num <= 0:
            print("Please enter a positive integer.")
        else:
            print_matrix(input_num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

