
import json
data = {
    "name":"jerry",
    "age":"19",
    "gender":"female"
}
print(type(data))
data1= json.dumps(data)
print(data1)
print(type(data1))     #data1为字符串的数据类型，创建字符串，只需要为变量赋值即可，如：Str = "hello world"

