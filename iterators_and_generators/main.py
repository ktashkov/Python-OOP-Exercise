class MyList:
    def __init__(self, my_list: list):
        self.my_list = my_list
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.my_list) - 1:
            raise StopIteration

        self.index += 1

        return self.my_list[self.index]


# a = iter([1, 2, 3])
#
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


# my_list = iter(MyList([1, 2, 3]))
#
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))
# print(next(my_list))

def add_one_to_number_in_list(numbers):  # [1, 2, 3]
    for num in numbers:
        yield num + 1


b = add_one_to_number_in_list([1, 2, 3])

for el in b:
    print(el)


print(sum(el for el in range(10)))