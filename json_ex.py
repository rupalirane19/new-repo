import json
import requests

# data = '{"name":"John", "age":30, "car":null}'
# a = json.loads(data)
# print(a)
#
# data1 = json.load (open('sample.json','r'))
# print(data1)
#
# d = json.dump(a,open('out.csv','w'))
# d1 = json.dumps(data1)
# print(d1)

r2 = requests.get("http://jsonplaceholder.typicode.com/todos")
data = json.loads(r2.text)
print(data)