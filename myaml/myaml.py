import ast
import astor
import yaml

from sympy.parsing.sympy_parser import parse_expr


class Evaluator(ast.NodeTransformer):
    __UNARY_OPS  = (ast.UAdd, ast.USub)
    __BINARY_OPS = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow)

    def __is_arithmetic(self, string):

        def _is_arithmetic(node):
            if isinstance(node, ast.Num):
                return True

            if isinstance(node, ast.Expression):
                return _is_arithmetic(node.body)

            if isinstance(node, ast.UnaryOp):
                valid_op = isinstance(node.op, Evaluator.__UNARY_OPS)
                return valid_op and _is_arithmetic(node.operand)

            if isinstance(node, ast.BinOp):
                valid_op = isinstance(node.op, Evaluator.__BINARY_OPS)
                return valid_op and _is_arithmetic(node.left) and _is_arithmetic(node.right)

            if isinstance(node, ast.Call):
                return all(map(_is_arithmetic, node.args))

            # unsupported node
            raise ValueError(f'Ignoring node {node}')

        try:
            return _is_arithmetic(ast.parse(string, mode='eval'))
        except (SyntaxError, ValueError):
            return False

    def __evaluate(self, expr):
        """
        Check for math expressions in lists.
        """
        if isinstance(expr, ast.List):
            expr = ast.List([self.__evaluate(x) for x in expr.elts])

        elif isinstance(expr, ast.Str) and self.__is_arithmetic(expr.s):
            val = round(float(parse_expr(expr.s)), 6)
            if val == int(val):
                val = int(val)
            expr = ast.Num(val)

        return expr

    def visit_Dict(self, node):
        """
        Return a new Dict node by evaluating the string values
        that contain math expressions.
        """
        # DFS traversal
        self.generic_visit(node)

        keys   = node.keys
        values = [self.__evaluate(v) for v in node.values]

        new_node = ast.Dict(keys, values)

        return ast.copy_location(new_node, node)


def safe_load(file_name: str) -> dict:
    """
    Load contents from @file_name, evaluating math expressions, if any.
    """
    with open(file_name, 'rt') as fp:
        contents = str(yaml.safe_load(fp))

    tree = Evaluator().visit(ast.parse(contents))
    src  = astor.code_gen.to_source(tree)
    out  = ast.literal_eval(src)

    return out


def dump(data, stream=None, **kwargs):
    """
    Simple and convenient wrapper over yaml.dump.
    """
    return yaml.dump(data, stream=stream, **kwargs)
