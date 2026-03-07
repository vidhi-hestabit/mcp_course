import asyncio
from my_mcp_client.mcp_client_class import MCPClient


async def main():
    async with MCPClient("http://127.0.0.1:8000/mcp/") as client:
        # res = await client.read_resource("file:///doc/my_python_file.py")
        # res1=await client.list_resources_template()
        # res2=await client.list_resources()
        # print("res1:", res1)

        # # print("res2:", res2)
        # # print("res:", res)
        # res=await client.read_resource("file:///doc/notes.txt")

        # res1=await client.read_resource("file:///doc/my_python_file.py")
        # print("res:", res.contents[0].text)
        # print("res1:", res1.contents[0].text)
        # res=await client.call_prompt(name="user_error_prompt", arguments={"error": "This is an error message"})
        # for item in res.messages:
        #     print("role:", item.role, "content:", item.content)

        res = await client.call_tool("plus", {"n1":300, "n2":100})

        for item in res.content:
            if item.type == "text":
                print("Tool result:", item.text)

asyncio.run(main())