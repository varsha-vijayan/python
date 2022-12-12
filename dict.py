age={"varsha":21,"silpa":22,"vidya":20,"jothy":21}
age_list=list(age.items())
age_list.sort()
print("In ascending order:",age_list)
age_list=list(age.items())
age_list.sort(reverse=True)
print("In decending order:",age_list)
dict=dict(age_list)
print("Dictionary is:",dict)
