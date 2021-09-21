def get_ranges(lst):
    segment = 0
    lst_temp = [[]]
    final_str = ''

    for num in range(len(lst)):
        if num != len(lst) - 1:
            if lst[num] + 1 == lst[num + 1]:
                (lst_temp[segment].append(lst[num]))
            elif lst[num] + 1 > lst[num + 1]:
                raise ValueError("The list should increase and not decrease")
            else:
                lst_temp.append([])
                lst_temp[segment].append(lst[num])
                segment += 1
        else:
            lst_temp[segment].append(lst[num])

    for el in lst_temp:
        if len(el) > 1:
            final_str += str(el[0]) + '-' + str(el[-1]) + ', '
        else:
            final_str += str(el[0]) + ', '

    final_str = final_str.rstrip(', ')

    return final_str

