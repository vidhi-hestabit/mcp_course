from mcp.server.fastmcp import FastMCP
from my_tool.math_tools import plus_function, subtract_function
from my_resource.my_doc import read_file_function

app=FastMCP(name="my_server", stateless_http=True)

@app.tool(name="plus", description="This is a plus function tool", title="Plus Function")
def plus(n1:int, n2:int)-> str:
    """This is plus function tool"""
    return plus_function(n1, n2)


@app.tool(description="This is a subtract function tool", title="Subtract Function")

async def tool_subtract(n1:int, n2:int)-> str:
    """This is subtract function tool"""
    return subtract_function(n1, n2)    

@app.resource("file:///doc/my_python_file.py", mime_type="text/x-python")
def read_file():
    """This function reads a python file and returns its content as a string"""
    return read_file_function()
    

mcp_app=app.streamable_http_app()