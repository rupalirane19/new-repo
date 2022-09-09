import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#     print("in string")
# else:
#     print("not in string")
#
# txt1 = "Roopali Rane Roop"
# x = re.findall("oop" , txt1)
# print(x)
#
# txt2 = "Roopali Rane Roop"
# x = re.split("\s" , txt2)
# print(x)
#
# txt3 = "Roopali Rane Roop"
# x = re.split("\t" , txt2)
# print(x)


txt3 = "Roopali Rane Roop"
x = re.findall("[a-z]" , txt3)
x1 = re.findall("R.." , txt3)

x3 = re.findall("R.*pali" , txt3)
x4= re.findall("R.+pali" , txt3)
x5= re.findall("R.?pali" , txt3)

x2 = re.findall("Roop$" , txt3)
if x2:
    print("find match")
else:
    print("not")

print(x)
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
