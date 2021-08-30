
def find_avg_marks(marks):
    sum_marks=sum(marks)
    total_subject=len(marks)
    avg_marks=sum_marks / total_subject

    return avg_marks
marks = [45,55,40,60]
avg_marks=find_avg_marks(marks)
print("your avg marks is:",avg_marks)



