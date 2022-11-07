def max_in_list(lst):
    first_max_number = 0
    cnt = 0

    for i in lst:
        if i > first_max_number:
            first_max_number = i
            print (first_max_number)
    return first_max_number

english_score = [ 33, 44, 55, 66, 77, 88, 99, 11, 22, 60]
result = max_in_list(english_score)
print('[3-1] 직접 구현한 max() : ', result)
print('[3-2] 내장 max()', max(english_score))