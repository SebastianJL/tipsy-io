"""Read and write tipsy files as numpy arrays. Tipsy is a binary data format used in [PKDGRAV3][pkdgrav3].

[pkdgrav3]: <https://bitbucket.org/dpotter/pkdgrav3/src/master/> "pkdgrav website"
"""
from .tipsy import Tipsy

__all__ = [Tipsy]
