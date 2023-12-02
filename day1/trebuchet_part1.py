numbers_to_sum = [];
with open('input.txt', 'r', encoding="utf-8") as f:
  for line in f:
    characters_in_line = list(line)
    numbers_in_line = list(filter(lambda a: a.isdigit(), characters_in_line))
    if (len(numbers_in_line) == 1):
      first_digit = second_digit = numbers_in_line[0]
      two_digit_num = int(first_digit + second_digit)
      numbers_to_sum.append(two_digit_num)
    else:
      first_digit = numbers_in_line.pop(0)
      second_digit = numbers_in_line.pop(-1)
      two_digit_num = int(first_digit + second_digit)
      numbers_to_sum.append(two_digit_num)
print(sum(numbers_to_sum))


    


# for every line in the file
#   filter numbers into list
#     pop first and last numbers
#       create new number with first and last digits
#       store number in list
# sum list