import array

def iterate():
    for i in range(3):
        yield i + 1

my_list = [*iterate()]
print(f"List: {my_list}")
print(f"List while index < 3: {my_list[:2]}")

rev1 = my_list[::-1]
print(f"Reversed copy: {rev1}")

rev1.reverse()
print(f"After reverse reversed copy: {rev1}")

print(f"List step 2: {my_list[::2]}")

extended_list = [0, *my_list, 4]
print(f"Extend left and right: {extended_list}")

print(f"Start extended from index == 1 with step 2: {extended_list[1::2]}")

arr = array.array('i', extended_list)
print(f"Span (Subview): {arr[1:3]}")

