import sys
sys.path.append('../')
import json
from wish import wish_methods
from joom import joom_methods
from amazon import amazon_methods

def get_method(request):
    content = request.get_argument("content",None)
    result = {"tip":"get successful","content":content}
    result = json.dumps(result)
    return result

def wish_execute_method(request):
    execute_method = request.get_argument("method",None)
    execute_type = request.get_argument("type",None)
    if method == "create":
        wish_methods.cread(method)
    elif method == "retrieve":
        pass
    elif method == "update":
        pass
    else:
        result == {"status_code":"0","error_message":"illegal execute"}
    result = json.dumps(result)
    return result   

def amazon_execute_method(request):
    result = amazon_methods.GetMatchingProduct()
    return result
    
def joom_execute_method(request):
    execute_method = request.get_argument("method",None)
    execute_type = request.get_argument("type",None)
    if method == "create":
        wish_methods.cread(method)
    elif method == "retrieve":
        pass
    elif method == "update":
        pass
    else:
        result == {"status_code":"0","error_message":"illegal execute"}
    result = json.dumps(result)
    return result
    