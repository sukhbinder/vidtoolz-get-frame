# vidtoolz-get-frame

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-get-frame.svg)](https://pypi.org/project/vidtoolz-get-frame/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-get-frame?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-get-frame/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-get-frame/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-get-frame/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-get-frame/blob/main/LICENSE)

Get frame out of a video for thumbnail

## Installation

First install [vidtoolz](https://github.com/sukhbinder/vidtoolz).

```bash
pip install vidtoolz
```

Then install this plugin in the same environment as your vidtoolz application.

```bash
vidtoolz install vidtoolz-get-frame
```
## Usage

type ``vid getframe --help`` to get help



## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd vidtoolz-get-frame
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
