# import csv
# with open("students.csv", "r", encoding="utf-8") as file:
#   print(file.read())

# import csv
# with open("students.csv", "r", encoding="utf-8") as file:
#    reader = csv.DictReader(file)
#    students = list(reader)
#    print(students)

# import csv
# with open("students.csv", "r", encoding="utf-8") as file:
#   reader = csv.DictReader(file)
#   students = list(reader)

# for s in students:
#   chinese = int(s["chinese"])
#   english = int(s["english"])
#   math = int(s["math"])
#   average = (chinese + english + math) / 3
#   print(s["name"], average)

import csv
max=0
total=0
mmax=0
with open("students.csv","r",encoding="utf-8")as file:
  reader = csv.DictReader(file)
  student=list(reader)
for s in student:
  c=int(s["chinese"])
  e=int(s["english"])
  m=int(s["math"])
  ave=(c+e+m)/3
  total += ave
  if(ave>max):
    max=ave
    t=s
  if(mmax<m):
    mmax=m
    x=s
  print(s["name"],"平均 :" ,ave)

print("最高平均 :",t["name"],max)
print("平均總分 :",total)
print("數學最高分 :",x["name"],mmax)

  
