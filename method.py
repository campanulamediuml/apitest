import json

def get_1():
    return 1+1

def post_method(request):
    content = request.get_argument("content",None)
    name = request.get_argument("name",None)
    json_string = {"received_1":content,"received_2":name}
    result = json.dumps(json_string)
    return result
    