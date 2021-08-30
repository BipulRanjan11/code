


# def find_avg_marks(marks):
#     sum_marks=sum(marks)
#     total_subject=len(marks)
#     avg_marks=sum_marks / total_subject
#
#     return avg_marks
# marks = [45,55,40,60]
# avg_marks=find_avg_marks(marks)
# print("your avg marks is:",avg_marks)
# def num(n1,n2):
#     print("the sum is",n1+n2)
#     print("the multiplication is :",n1*n2)
# num(5,4)


# def check_prime_number():
#     num=int(input("Enter your no,:"))
#     for i in range(2,num):
#             if num % i == 0:
#                  print(num,"is not prime")
#                  break
#             else:
#              print(num,"is prime")
#             break
#
#
# check_prime_number()

# def factorial(num):
#
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return num*factorial(num-1)
# num=5
# fact=factorial(num)
#
# print("the factorial of",num, 'is',fact)

# def is_leap(year):
#
#
#     # Write your logic here
#     if year % 400 == 0:
#         leap = True
#     elif year % 100 == 0 :
#         leap=False
#     elif year % 4 == 0:
#         leap = True
#     else:
#         leap=False
#     return leap
#
#
# year = int(input())
# print(is_leap(year))


# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# output = []
# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if i + j + k == n:
#                 continue
#             else:
#                 output.append([i, j, k])
#
# print(output)



# with open("example.txt","r") as f:
#     f.seek(2)
#     print(f.read())
#     print(f.tell())


# from array import *
# a1=array('i',[4,5,6,8,9])
# a1.insert(2,45)
# y=a1[1:6]
# for i in y:
#   print(i,end=' ')
#
#



class Triangle:
  def __init__(self,a,b,c):
    self.a=a
    self.b=b
    self.c=c

  def cal_perimeter(self):
      perimeter=self.a+self.b+self.c
      return perimeter

t1=Triangle(2,4,5)
t2=Triangle(4,2,8)
result=t1.cal_perimeter()
result2=t2.cal_perimeter()
print(result,result2)



#Guess The Number Game





