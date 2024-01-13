# pycharcounts_cz

Calculate the number of characters in a text file.

## Installation

```bash
$ pip install pycharcounts_cz
```

## Usage

`pycharcounts_cz` can be used to count characters in a text file 
and present results as follows:

```python
from pycharcounts_cz.pycharcounts_cz import count_characters
from pycharcounts_cz.output import full_output
import pandas as pd

file_path = "test.txt"  # path to your file
count = count_characters(file_path)
full_output(file_path, count)
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pycharcounts_cz` was created by Celeste Zhao. It is licensed under the terms of the MIT license.

## Credits

`pycharcounts_cz` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
