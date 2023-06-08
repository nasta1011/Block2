
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def binary_search (list_seq, user_number):
    left = -1
    right = len(list_seq)
    while right - left > 1:
        middle = (left + right) // 2
        if list_seq[middle] < user_number:
            left = middle
        else:
            right = middle
    if right == len(list_seq):
        return None
    else:
        return left, right

try:
    list_seq = list(map(int, input("Введите последовательность чисел: ").split()))
except ValueError:
    print("Ошибка ввода данных. Проверьте правильность введенной последовательности чисел. ")
else:
    list_seq = merge_sort(list_seq)
    print("Отсортированный список:", list_seq)

    try:
        user_number = int(input("Введите любоє число: "))
    except ValueError:
        print("Ошибка ввода данных. Проверьте правильность введенного числа.")
    else:
        result = binary_search(list_seq, user_number)
        if result is None:
            print("В списке нет элемента, меньшего числа", user_number, "или следующего за ним элемента. ")
        else:
            print("Позиция элемента, меньшего", user_number, ":", result[0])
            print("Позиция элемента, большего или равного",user_number, ":", result[1])