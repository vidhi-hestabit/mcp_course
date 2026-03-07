from mcp import ClientSession
from typing import Optional
from contextlib import AsyncExitStack
from mcp.client.streamable_http import streamable_http_client

class MCPClient:

    def __init__(self, url:str):
        self.session: Optional[ClientSession]=None
        self.exit_stack=AsyncExitStack()
        self.url=url


    async def __aenter__(self):
        print("Enter session")
        read, write,_ = await self.exit_stack.enter_async_context(streamable_http_client(self.url))
        self.session=await self.exit_stack.enter_async_context(ClientSession(read, write))
        await self.session.initialize()
        return self
    
    async def __aexit__(self, *args):
        print("Exit session")
        await self.exit_stack.aclose()

    async def my_tools(self):
        response=await self.session.list_tools()
        tools=response.tools
        print("\n Connected tools:", [tool.name for tool in tools])

    async def plus_method(self, tool_name:str, arg:dict):
        res=await self.session.call_tool(name=tool_name, arguments=arg)
        return res
    
    async def list_resources(self):
        res=await self.session.list_resources()
        return res.resources
    
    async def list_resources_template(self):
        res=await self.session.list_resource_templates()
        resources= res.resourceTemplates
        print("\n Connected resource templates:", [resource.name for resource in resources])
    

    async def read_resource(self, uri:str):
        res=await self.session.read_resource(uri=uri)
        return res
    
    async def list_prompts(self):
        res=await self.session.list_prompts()
        prompts=res.prompts
        print("\n Connected prompts:", [prompt.name for prompt in prompts])

    async def call_prompt(self, name:str, arguments:dict):
        res=await self.session.get_prompt(name=name, arguments=arguments)
        return res
    
    async def plus(self):
        return "Plus working..."
    
