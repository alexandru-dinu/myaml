# myaml

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/alexandru-dinu/myaml/blob/master/LICENSE)

<!-- [![pypi](https://img.shields.io/pypi/v/myaml.svg)](https://pypi.org/project/myaml/) -->

M(ath)YAML: evaluate math expressions in YAML files.

<!-- ## Instal
```bash
pip install myaml
``` -->

## Usage

`myaml` allows you to define math expressions in YAML files:
```yaml
# test.yaml
---
- x1:
    x: 2**(3 - 1)
    y: (12 % 9) - sqrt(9)
- x2:
    x: (2**3) - 1
    y: 12 % (9 - sqrt(4))
```
which will be evaluated at load-time:
```python
>>> import myaml
>>> xs = myaml.safe_load('test.yaml')
>>> xs
[
    {"x1": {"x": 4, "y": 0}},
    {"x2": {"x": 7, "y": 5}}
]
```

Expressions should be [SymPy compatible](https://docs.sympy.org/latest/tutorial/basic_operations.html), since [`parse_expr`](https://docs.sympy.org/latest/modules/parsing.html#sympy.parsing.sympy_parser.parse_expr) is used for evaluation.