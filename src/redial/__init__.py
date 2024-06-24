# -*- coding: utf-8 -*-
from importlib.metadata import distribution, PackageNotFoundError

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = distribution(dist_name).version
except PackageNotFoundError:
    __version__ = 'unknown'
finally:
    del distribution, PackageNotFoundError
