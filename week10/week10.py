# mylist = [76, 92.3, "hello", True, 4, 76]
#
# print(mylist)
#
# mylist.append("apple")
# mylist.append(76)
# print(mylist)
#
# mylist.insert(3, "cat")
# print(mylist)
#
# mylist.insert(0,99)
# print(mylist)
#
# print(mylist.index("hello"))
#
# print(mylist.count(76))
#
# mylist.remove(76)
# print(mylist)
#
# mylist.pop(mylist.index(True))
# print(mylist)

# def sum_of_squares(numbers):
#     sum = 0
#     for number in numbers:
#         sum += number ** 2
#     return sum
#
# my_list = [3, 4, 5]
# print(sum_of_squares(my_list))

# def sum_evens(num_list):
#     sum = 0
#     for num in num_list:
#         if num % 2 == 0:
#             sum += num
#     return sum
#
# print(sum_evens([1,2,3,4,5,6,7,8,9,10]))
#
# def count_five_letter(words):
#     counter = 0
#     for word in words:
#         if len(word) == 5:
#             counter += 1
#     return counter
#
# print(count_five_letter(["hello", "world", "world", "world", "world", "world", "ali"]))

# def sum_until_even(num_list):
#     total = 0
#     for num in num_list:
#         if num % 2 == 0:
#             break
#         total += num
#     return total
#
# print(sum_until_even([1, 2, 3, 4, 5, 6, 7]))

# def count_until_sam(words):
#     count = 0
#     for word in words:
#         count += 1
#         if word == 'sam':
#             break
#     return count
#
# my_list = ["ali", "ahmet", "fatma", "kelly", "sam", "ela"]
# print(count_until_sam(my_list))

# def replace(s, old, new):
#     pieces = s.split(old)
#     print(pieces)
#     print(new.join(pieces))
#     return new.join(pieces)
#
# def test(actual, expected):
#     if actual != expected:
#         print("PASSED")
#     else:
#         print("FAILED")
#
#
# test(replace('Mississippi',  "i", "I") , 'MIssIssIppI')
#
#
# def find_max_val_in_list(num_list):
#     max_val = num_list[0]
#     for num in num_list:
#         if num > max_val:
#             max_val = num
#     return max_val
#
# my_list = [3,2,1,0,5,7,8,10,2]
# print(find_max_val_in_list(my_list))
# new_list = [-34, -48, -42, -1907, -2]
# print(find_max_val_in_list(new_list))