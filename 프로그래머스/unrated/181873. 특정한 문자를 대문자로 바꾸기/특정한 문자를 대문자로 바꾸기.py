def solution(my_string, alp):
    if alp in my_string:
        alp_new = alp.upper()
        return my_string.replace(alp,alp_new)
    else:
        return my_string