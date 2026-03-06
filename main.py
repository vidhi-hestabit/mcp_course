from mcp.server.fastmcp import FastMCP
from my_tool.math_tools import plus_function, subtract_function

app=FastMCP(name="my_server", stateless_http=True)

@app.tool(name="plus", description="This is a plus function tool", title="Plus Function")
def plus(n1:int, n2:int)-> str:
    """This is plus function tool"""
    return plus_function(n1, n2)


@app.tool(description="This is a subtract function tool", title="Subtract Function")

async def tool_subtract(n1:int, n2:int)-> str:
    """This is subtract function tool"""
    return subtract_function(n1, n2)    

mcp_app=app.streamable_http_app()