from mcp.server.fastmcp.prompts import base

def hello(user_name: str, query: str = None):
    """Hello prompt"""
    return f"Hello my name is {user_name}. {query if query else ''}"

def user_error(error: str):
    """Error prompt"""
    return [
        base.UserMessage(content="I am facing an error"),
        base.UserMessage(content=error),
        base.AssistantMessage(content="I am here to help you with the error")
    ]