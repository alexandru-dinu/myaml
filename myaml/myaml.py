import yaml
from sympy.parsing.sympy_parser import parse_expr


class ExprLoader(yaml.SafeLoader):
    def __init__(self, stream):
        super().__init__(stream)
        self.add_constructor(tag='!eval', constructor=self.evaluate)

    @staticmethod
    def evaluate(loader, node):
        expr = loader.construct_scalar(node)

        try:
            val = round(float(parse_expr(expr)), 6)
            if val == int(val):
                val = int(val)
        except (ValueError, TypeError):
            return expr

        return val


def safe_load(file_name: str) -> dict:
    """
    Load contents from @file_name, evaluating math expressions, if any.
    """
    with open(file_name, 'rt') as fp:
        contents = yaml.load(fp, ExprLoader)

    return contents


def dump(data, stream=None, **kwargs) -> str:
    """
    Simple and convenient wrapper over yaml.dump.
    """
    return yaml.dump(data, stream=stream, **kwargs)
