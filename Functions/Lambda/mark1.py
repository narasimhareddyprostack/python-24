marks = [35,36,37,38,39,40]

def addOneMark(mark):
    return mark+1

new_Marks=list(map(addOneMark, marks))
print(new_Marks)