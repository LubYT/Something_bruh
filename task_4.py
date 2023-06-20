def Check_Palindrom(word):
    result=True
    for tick in range(len(word)//2):
        check_last = word[::-(tick+1)]
        check_first = word[::(tick+1)]
        if check_first == check_last:
          result=True
        else:
          result = False
          return result
    return result
result_word=Check_Palindrom('eye')
print(result_word)