# terminal

This project contains a module that can be used as a beautiful terminal printer.

### Requirements

Python 3.7 and later is supported.

### Install using pip

You can install the latest stable release of gvm-tools from the Python Package
Index using [pip](https://pip.pypa.io/):

    pip install --user terminal

## Maintainer

This project is maintained by Jaspar Löchte ([Greenbone Networks GmbH](https://www.greenbone.net/)).

## Contributing

Your contributions are highly appreciated. Please
[create a pull request](https://github.com/greenbone/gvm-tools/pulls) on GitHub.
For bigger changes, please discuss it first in the
[issues](https://github.com/greenbone/gvm-tools/issues).

For development you should use [poetry](https://python-poetry.org/)
to keep you python packages separated in different environments. First install
poetry via pip

    pip install --user poetry

Afterwards run

    poetry install

in the checkout directory of `terminal` (the directory containing the
`pyproject.toml` file) to install all dependencies including the packages only
required for development.

Afterwards active the git hooks for auto-formatting and linting via
[autohooks](https://github.com/greenbone/autohooks).

    poetry run autohooks activate --force

## License

Copyright (C) 2022 [Greenbone Networks GmbH](https://www.greenbone.net/)

Licensed under the [GNU General Public License v3.0 or later](LICENSE).
