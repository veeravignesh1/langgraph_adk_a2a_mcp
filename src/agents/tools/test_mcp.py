from fastmcp import FastMCP

mcp = FastMCP("Demo")


@mcp.tool
def add(self, a: float, b: float) -> float:
    return a + b


@mcp.tool
def subtract(self, a: float, b: float) -> float:
    return a - b


@mcp.tool
def multiply(self, a: float, b: float) -> float:
    return a * b


@mcp.tool
def divide(self, a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


if __name__ == "__main__":
    mcp.run(transport="stdio", host="0.0.0.0", port=8000)

# To run the server, use:
# uv run --with fastmcp src/agents/tools/test_mcp.py

# To run the server, use:
