def min_in_list(lst):
    min = lst[0]
    for i in lst[1:]:
        if i < min:
            min = i
    return min

english_score = [ 33, 44, 55, 66, 77, 88, 99, 11, 22, 60]
result = min_in_list(english_score)
print('[3-1] 직접 구현한 min() : ', result)
print('[3-2] 내장 min()', min(english_score))