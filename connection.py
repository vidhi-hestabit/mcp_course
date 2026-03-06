import asyncio
from my_mcp_client.mcp_client_class import MCPClient


async def main():
    async with MCPClient("http://127.0.0.1:8000/mcp/") as client:
        res = await client.plus_method("plus", {"a": 5, "b": 3})
        print(res)
        

asyncio.run(main())