def swap(str):
    start=str[0]
    end=str[-1]
    swap=end+str[1:-1]+start
    print("the string is:",str)
    print("the swapped string is:",swap)
swap("python")
