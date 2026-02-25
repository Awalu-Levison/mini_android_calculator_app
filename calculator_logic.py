import ast
import operator

"""Define Calculator operators"""
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

"""Define the calculator brain"""
class CalculatorEngine:

    """mathematical expression safely"""
    def evaluate(self, expression):
        try:
            node = ast.parse(expression, mode='eval').body
            return str(self._eval(node))
        except Exception:
            return "Error"

    """
    Define method _evalEvaluate node 
    Node = (Represents mathematical expression)
    This avoids security issues and keeps dependencies zero
    """
    def _eval(self, node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Binop):

            return OPERATORS[type(node.op)](
                    self._eval(node.left),
                    self._evval(node.right)
            )
        else:
            raise TypeError(node)
