def find_multiple_of_three(start, end):

    return [i for i in range(start, end + 1) if i % 3 == 0]

input_start = int(input("Enter the start of the range: "))
input_end = int(input("Enter the end of the range: "))
result = find_multiple_of_three(input_start, input_end)

print(f"The multiples of 3 between {input_start} and {input_end} are: {result}")

