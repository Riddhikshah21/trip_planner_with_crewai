from langchain.tools import tool

class CalculatorTools:
    @staticmethod
    @tool("Perform calculation")
    def calculate(opr):
        try:
            return eval(opr)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression!"