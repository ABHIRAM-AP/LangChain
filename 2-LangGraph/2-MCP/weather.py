from fastmcp import FastMCP 

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(loc:str)->str:
    """_summary_
    Get the weather location
    """
    return f"It's sunny in {loc}"




if __name__ == "__main__":
    mcp.run(transport="streamable-http")