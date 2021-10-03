import copy

num_list = [1, 2, 3, [1, 2, 3], 4]
copy_test = copy.copy(num_list)
deepcopy_test = copy.deepcopy(num_list)
num_list[3].append(4)
print(copy_test)
print(deepcopy_test)

from functools import lru_cache


@lru_cache()
def change_money(total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    return change_money(total - 2) + change_money(total - 3) + \
           change_money(total - 5)
print(change_money(99))