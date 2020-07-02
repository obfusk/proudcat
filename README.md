<!-- {{{1 -->

    File        : README.md
    Maintainer  : Felix C. Stegerman <flx@obfusk.net>
    Date        : 2020-07-02

    Copyright   : Copyright (C) 2020  Felix C. Stegerman
    Version     : v0.2.0
    License     : GPLv3+

<!-- }}}1 -->

[![PyPI Version](https://img.shields.io/pypi/v/proudcat.svg)](https://pypi.python.org/pypi/proudcat)
[![GPLv3+](https://img.shields.io/badge/license-GPLv3+-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)

## Description

proudcat - cat + :rainbow:

proudcat is basically a variant of
[`proudcat-rust`](https://github.com/obfusk/proudcat-rust) /
[`pridecat`](https://github.com/lunasorcery/pridecat)
written in python.

![screenshot](screenshot.png)

![screenshot](screenshot-bg-frame.png)

## Help

```bash
$ proudcat --help
```

## Requirements

Python >= 3.5 + click.

## Installing

### Using pip

```bash
$ pip install proudcat
```

### Manually

Install the dependencies (as e.g. debian packages or using `pip`):

```bash
$ apt install python3-click       # debian/ubuntu
$ pip install click               # pip
```

Then just put `proudcat` somewhere on your `$PATH` (e.g. `~/bin`).

## License

[![GPLv3+](https://www.gnu.org/graphics/gplv3-127x51.png)](https://www.gnu.org/licenses/gpl-3.0.html)

<!-- vim: set tw=70 sw=2 sts=2 et fdm=marker : -->
