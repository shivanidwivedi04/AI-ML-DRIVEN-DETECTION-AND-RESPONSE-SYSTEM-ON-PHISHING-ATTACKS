def count_upper_chars():
    num_inputs = int(input("Enter the number of inputs: "))
    for _ in range(num_inputs):
        s = input("Enter a string: ")
        upper_count = sum(1 for c in s if c.isupper())
        print(upper_count)

count_upper_chars()