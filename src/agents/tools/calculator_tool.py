from fastmcp import FastMCP

from core.settings import settings

mcp = FastMCP("Demo")


@mcp.tool
def add(a: float, b: float) -> float:
    """
    Adds two numbers and returns the result.
    Args:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The sum of a and b.
    """
    return a + b


@mcp.tool
def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first and returns the result.
    Args:
        a (float): The number to subtract from.
        b (float): The number to subtract.
    Returns:
        float: The result of a - b.
    """
    return a - b


@mcp.tool
def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers and returns the result.
    Args:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The product of a and b.
    """
    return a * b


@mcp.tool
def divide(a: float, b: float) -> float:
    """
    Divides the first number by the second and returns the result.
    Args:
        a (float): The numerator.
        b (float): The denominator (must not be zero).
    Returns:
        float: The result of a / b.
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


app = mcp.http_app(path=f"{settings.mcp_prefix}/mcp")

## Transport: HTTP
# Option 1:
# Define this as a app and run it with uvicorn (Production recommended)
# uvicorn  src.agents.tools.calculator_tool:app --host 0.0.0.0 --port 8000

# Option 2:
# Run it with python for local dev / fast iteration
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)

## Transport: STDIO
# if __name__ == "__main__":
#     mcp.run(transport="stdio")
