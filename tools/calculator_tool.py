from langchain.tools import tool

# class CalculatorTools(BaseTool):
    
@tool("Perform Calculation")
def calculate(opr):
    """
    Perform a calculation based on the provided mathematical expression.

    Args:
        expression (str): A string representing a mathematical expression (e.g., "2 + 2").

    Returns:
        str: The result of the calculation as a string.
    """
    try:
        result = eval(opr)
        return str(result)
    except SyntaxError:
        return "Error: Invalid syntax in mathematical expression!"