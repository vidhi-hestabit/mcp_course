import requests

url="http://127.0.0.1:8000/mcp/"

headers = {
    "Accept": "application/json, text/event-stream"
}

body = {
    "jsonrpc": "2.0",
    "method": "prompts/get",
    "params":{
        # "uri": "file:///doc/my_python_file.py"
        "name" :"user_error_prompt",
        "arguments":{
            "error": "Python error"
        }   
        #     "n1": 500,
        #     "n2": 300
    },
    "id": 2
}

res=requests.post(url=url, headers=headers, json=body)

result=res.text

print(result)
