import json


def json_python():
    # "将json转换为python"
    js = {
        "name":"菜鸟教程"  ,
          }
    rest = json.dumps(js)
    print(rest)

d = json_python()
print(d)

# if __name__ == '_main_':
#     json_python()




