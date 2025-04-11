# vidtoolz-get-frame

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-get-frame.svg)](https://pypi.org/project/vidtoolz-get-frame/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-get-frame?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-get-frame/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-get-frame/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-get-frame/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-get-frame/blob/main/LICENSE)

Get frame out of a video for thumbnail

![vidtoolz-get-frame demo](https://raw.githubusercontent.com/sukhbinder/vidtoolz-get-frame/refs/heads/main/demo.png)

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

```bash

usage: vid getframe [-h] [-n NUM] [-o OUTDIR] [-t [TIMES ...]] fname

Get frame out of a video for thumbnail

positional arguments:
  fname                 MOV Mp4 file from which frames has to be extracted

optional arguments:
  -h, --help            show this help message and exit
  -n NUM, --num NUM     No of frames to collect
  -o OUTDIR, --outdir OUTDIR
                        Output dir
  -t [TIMES ...], --times [TIMES ...]
                        Specific times in seconds to extract frames.


```

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
