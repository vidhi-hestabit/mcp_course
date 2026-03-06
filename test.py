import requests

url="http://127.0.0.1:8000/mcp/"

headers = {
    "Accept": "application/json, text/event-stream"
}

body = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params":{
        "name" :"tool_subtract",
        "arguments":{
            "n1": 500,
            "n2": 300
        }
    },
    "id": 2
}

res=requests.post(url=url, headers=headers, json=body)

result=res.text

print(result)
