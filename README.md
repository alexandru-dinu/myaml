# myaml

[![workflow](https://github.com/alexandru-dinu/myaml/workflows/CI/badge.svg)](https://github.com/alexandru-dinu/myaml/actions?query=workflow%3ACI)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/alexandru-dinu/myaml/blob/master/LICENSE)
[![pypi](https://img.shields.io/pypi/v/myaml.svg)](https://pypi.org/project/myaml/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

M(ath)YAML: evaluate math expressions in YAML files.

## Install
```bash
pip install myaml
```

## Usage

`myaml` allows you to define math expressions in YAML files:
```yaml
# test.yaml
---
- x1:
    x: !eval 2**(3 - 1)
    y: !eval (12 % 9) - sqrt(9)
- x2:
    x: !eval (2**3) - 1.0
    y: !eval -0.75 ** (9 - cos(3.1415) * log(2.718))
- x3:
    x: hello world
    y: /this/is/a/path
```

Expressions annotated with `!eval` tag will be evaluated at load-time.
Any other strings will be left intact:

```python
>>> import myaml
>>> xs = myaml.safe_load('test.yaml')
>>> xs
[
    {'x1': {'x': 4, 'y': 0}},
    {'x2': {'x': 7, 'y': -0.056315}},
    {'x3': {
        'x': 'hello world',
        'y': '/this/is/a/path'
    }}
]
```

## Notes

- `myaml` supports arbitrary nesting, conforming with YAML spec.
- `myaml` is built on top of [PyYAML's `safe_load`](https://pyyaml.org/wiki/PyYAMLDocumentation).
- expressions should be [SymPy compatible](https://docs.sympy.org/latest/tutorial/basic_operations.html), since [`parse_expr`](https://docs.sympy.org/latest/modules/parsing.html#sympy.parsing.sympy_parser.parse_expr) is used for evaluation.
