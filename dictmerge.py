def merge(dict1,dict2):
    return(dict1.update(dict2))
dict1={"a":10,"b":20}
dict2={"c":30,"d":40}
print("The first dictionary is:",dict1)
print("The second dictionary is:",dict2)
(merge(dict1,dict2))
print("The dictionaries after merge:",dict1)
