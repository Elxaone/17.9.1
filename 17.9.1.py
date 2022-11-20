sequence = input("Введите последовательность чисел через пробел: ")
sequence_mod = [int(a) for a in sequence.split()]
if ' ' not in (sequence):
    raise ValueError("Введены некорректные данные! Введите последовательность чисел через пробел!")

num = int(input("Введите любое число: "))
while num > max(sequence_mod) or num < min(sequence_mod):
    print("Число не входит в последовательность")
    num = int(input("Введите другое число "))

sequence_mod.append(num)

for i in range(1, len(sequence_mod)):
    x = sequence_mod[i]
    idx = i
    while idx > 0 and sequence_mod[idx - 1] > x:
        sequence_mod[idx] = sequence_mod[idx - 1]
        idx -= 1
    sequence_mod[idx] = x
print("Сортированный список:", sequence_mod)


def binary_search(sequence_mod, num, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if sequence_mod[middle] == num:
        return middle
    elif num < sequence_mod[middle]:
        return binary_search(sequence_mod, num, left, middle - 1)
    else:
        return binary_search(sequence_mod, num, middle + 1, right)


binary = int(binary_search(sequence_mod, num, 0, len(sequence_mod) - 1))
print(binary - 1, binary + 1)
