import json
import wish.method

def get_method(request):
    content = request.get_argument("content",None)
    result = {"tip":"get successful","content":content}
    result = json.dumps(result)
    return result

def wish_execute(request):
    method = request.get_argument("method",None)
    if method == "create":
        pass
    elif method == "retrieve":
        pass
    elif method == "update":
        pass
    else:
        result == {"status_code":"0","error":"illegal execute"}
    result = json.dumps(result)
    return result
    