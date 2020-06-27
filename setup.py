from pathlib import Path
from setuptools import setup

import proudcat

long_description    = Path(__file__).with_name("README.md") \
                      .read_text(encoding = "utf8")

setup(
  name              = "proudcat",
  url               = "https://github.com/obfusk/proudcat",
  description       = "proudcat - cat + :rainbow:",
  long_description  = long_description,
  long_description_content_type = "text/markdown",
  version           = proudcat.__version__,
  author            = "Felix C. Stegerman",
  author_email      = "flx@obfusk.net",
  license           = "GPLv3+",
  classifiers       = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Utilities",
  ],
  keywords          = "cat cli terminal colors colours",
  scripts           = ["proudcat"],
  python_requires   = ">=3.5",
  install_requires  = ["click>=6.0"],
)
