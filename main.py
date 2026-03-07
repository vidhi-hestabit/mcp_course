from mcp.server.fastmcp import FastMCP, Context
from mcp.server.session import ServerSession
from mcp.types import SamplingMessage, TextContent

from my_tool.math_tools import plus_function, subtract_function
from my_resource.my_doc import read_file_function, read_file_function_dynamic
from my_prompt.error_prompt import hello, user_error

app = FastMCP(name="my_server")


@app.tool(name="plus", description="This is a plus function tool")
async def plus(n1: int, n2: int, ctx: Context[ServerSession, None]) -> str:

    prompt = plus_function(n1, n2)

    result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(type="text", text=prompt)
            )
        ],
        max_tokens=100
    )

    if result.content.type == "text":
        return result.content.text

    return str(result.content)


@app.tool()
async def tool_subtract(n1: int, n2: int) -> str:
    return subtract_function(n1, n2)

@app.resource("file:///doc/my_python_file.py", mime_type="text/x-python")
def read_file():
    return read_file_function()


@app.resource("file:///doc/{path}", mime_type="text/plain")
async def read_file_dynamic(path: str):
    return read_file_function_dynamic(path)


@app.prompt()
def hello_prompt(user_name: str, query: str = None):
    return hello(user_name, query)


@app.prompt()
async def user_error_prompt(error: str):
    return await user_error(error)


mcp_app = app.streamable_http_app()