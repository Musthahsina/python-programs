'''json module--storing and exchanging
of data'''


import json
x={'name':'priya','age':12}
print(type(x))
y=json.dumps(x)
print(y)
print(type(y))
x='{"name":"priya","age":12}'
print(type(x))
y=json.loads(x)
print(y)
print(type(y))
d=dir(json)
print(d)
'''acess the key2 in json'''

x='{"name":"priya","age":12,"course":"python"}'
y=json.loads(x)
print(y["age"])

'''acess salary '''
import json
samp="""{"company":{"employee":{"name":"emma","payble":{"salary":7000,"bonus":800}}}}"""
s=json.loads(samp)
print(s["company"]["employee"]["payble"]["salary"])

