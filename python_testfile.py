def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers and return the result.
    """
    return a + b


def greet(name: str) -> str:
    """
    Return greeting message.
    """
    return f"Hello, {name}! Welcome to GitHub MCP Server."


if __name__ == "__main__":

    result = add_numbers(10, 20)
    print("Addition Result:", result)

    message = greet("Aruna")
    print(message)
