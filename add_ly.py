def add_string(str):
    length=len(str)
    if length>2:
        if str[-3:]=='ing':
            str+='ly'
        else:
            str+='ing'
    return str
print(add_string('walking'))
