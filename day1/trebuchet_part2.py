import re

numbers_to_sum = [];

def extract_numbers(input_str):
    # Replace number words with a modified version for easy extraction
    replacements = {
        'zero': 'z0o',
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e'
    }

    for word, replacement in replacements.items():
        input_str = input_str.replace(word, replacement)

    # Use regular expression to extract numbers
    numbers = re.findall(r'\d', input_str)

    # Convert extracted numbers back to integers
    numbers = [int(num) for num in numbers]

    return numbers

with open('input.txt', 'r', encoding="utf-8") as f:
  for line in f:
    numbers_in_line = extract_numbers(line)
    if (len(numbers_in_line) == 1):
      first_digit = second_digit = numbers_in_line[0]
      two_digit_num = int(str(first_digit) + str(second_digit))
      numbers_to_sum.append(two_digit_num)
    else:
      first_digit = numbers_in_line.pop(0)
      second_digit = numbers_in_line.pop(-1)
      two_digit_num = int(str(first_digit) + str(second_digit))
      numbers_to_sum.append(two_digit_num)
print(sum(numbers_to_sum))


# for every line in the file
#   identify numbers from digits and words
#   filter numbers into list
#     pop first and last numbers
#       create new number with first and last digits
#       store number in list
# sum list

# extract numbers from words
#   replace each identified word with first_char + num + last_char
#     ex: sevenine -> s7nn9e
#   filter numbers
#     ex: s7nn9e -> [7, 9]