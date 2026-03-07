from mcp import ClientSession, CreateMessageResult
from typing import Optional
from contextlib import AsyncExitStack
from mcp.client.streamable_http import streamable_http_client
from mcp.types import TextContent, CreateMessageRequestParams
from mcp.shared.context import RequestContext


class MCPClient:

    def __init__(self, url: str):
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.url = url

    


    async def mock_llm(
        self,
        context: RequestContext[ClientSession, None],
        params: CreateMessageRequestParams
    ) -> CreateMessageResult:

        print("params -----> ", params)

        return CreateMessageResult(
            role="assistant",
            content=TextContent(type="text", text="This is a mock response from the LLM"),
            model="gemini"
        )

    async def __aenter__(self):
        print("Enter session")

        print("Connecting to MCP server...")
        read, write, _ = await self.exit_stack.enter_async_context(
            streamable_http_client(self.url)
        )

        print("Creating client session...")
        self.session = await self.exit_stack.enter_async_context(
            ClientSession(read, write, sampling_callback=self.mock_llm)
        )

        print("Initializing session...")
        await self.session.initialize()

        print("Session initialized")

        return self

    async def __aexit__(self, *args):
        print("Exit session")
        await self.exit_stack.aclose()

    async def my_tools(self):
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected tools:", [tool.name for tool in tools])

    async def call_tool(self, tool_name: str, arg: dict):
        res = await self.session.call_tool(name=tool_name, arguments=arg)
        return res

    async def list_resources(self):
        res = await self.session.list_resources()
        return res.resources

    async def list_resources_template(self):
        res = await self.session.list_resource_templates()
        resources = res.resource_templates
        print("\nConnected resource templates:", [r.name for r in resources])

    async def read_resource(self, uri: str):
        res = await self.session.read_resource(uri=uri)
        return res

    async def list_prompts(self):
        res = await self.session.list_prompts()
        prompts = res.prompts
        print("\nConnected prompts:", [p.name for p in prompts])

    async def call_prompt(self, name: str, arguments: dict):
        res = await self.session.get_prompt(name=name, arguments=arguments)
        return res

    async def plus(self):
        return "Plus working..."