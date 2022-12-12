def occur(str):
    first_char=str[0]
    str=str.replace(first_char,"$")
    str=first_char+str[1: ]
    return str
print(occur("onion"))
