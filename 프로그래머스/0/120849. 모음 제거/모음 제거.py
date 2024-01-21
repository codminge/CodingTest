def solution(my_string):
    answer = []
    vowel = "aeiou"
    for i in vowel:
        if i in my_string:
            my_string = my_string.replace(i,"")
    return my_string