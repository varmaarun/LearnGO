def anagrams(word, words):
    sorted_word=sorted(word)
    #print(sorted_word)
    lst=[]
    for each in words:
        each_sorted=sorted(each)
        if each_sorted==sorted_word:
            lst.append(each)

    return lst
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
#assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])