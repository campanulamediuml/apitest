import sys
sys.path.append('../')
import json
from wish import wish_methods
from joom import joom_methods

def get_method(request):
    content = request.get_argument("content",None)
    result = {"tip":"get successful","content":content}
    result = json.dumps(result)
    return result


# json_request = {"method":"",xxxx}

def wish_execute(request):
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
    