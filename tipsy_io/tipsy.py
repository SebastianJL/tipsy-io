from typing import Optional
import numpy as np
import numpy.typing as npt
from dataclasses import dataclass, field

header_type = np.dtype([('time', '>f8'), ('n', '>i4'), ('dims', '>i4'),
                       ('n_gas', '>i4'), ('n_dark', '>i4'), ('n_star', '>i4'), ('pad', '>i4')])
_ALLOWED_BYTEORDERS = ('=', '>', '<')
_ALLOWED_DIMS = (1, 2, 3)


@dataclass
class Tipsy:
    header: npt.DTypeLike
    gas: np.array = field(repr=False)
    dark: np.array = field(repr=False)
    star: np.array = field(repr=False)

    def tofile(self, fname: str):
        with open(fname, 'wb') as ofile:
            self.header.tofile(ofile)
            self.gas.tofile(ofile)
            self.dark.tofile(ofile)
            self.star.tofile(ofile)

    @classmethod
    def fromfile(cls, fname: str, byteorder: Optional[str] = None) -> "Tipsy":
        f"""Load tipsy file as Tipsy object.

        Args:
            fname: File name or path.
            byteorder: Endianness of binary file. Allowed values are {_ALLOWED_BYTEORDERS} or None.
                See https://numpy.org/doc/stable/reference/generated/numpy.dtype.byteorder.html for explanation.
                If byte order is {None} then Tipsy tries to guess the byteorder in order of {_ALLOWED_BYTEORDERS}. 
                Defaults to None.

        Raises:
            KeyError: Invalid byteorder.
            IOError: Couldn't load file with specified byteorder.
            IOError: Couldn't guess byteorder.

        Returns:
            Self
        """
        if byteorder not in _ALLOWED_BYTEORDERS + (None,):
            raise KeyError(
                f'byteorder must be one of {_ALLOWED_BYTEORDERS} or {None}')

        with open(fname, 'rb') as binary_in:
            # Explicitly defined byte order.
            if byteorder is not None:
                binary_in.seek(0)
                header = np.fromfile(
                    binary_in, count=1, dtype=header_type.newbyteorder(byteorder))[0]
                n_dims = header['dims']
                if n_dims not in _ALLOWED_DIMS:
                    raise IOError(
                        f"Couldn't open file with {byteorder = }: {fname}")
            # Determine byte order from file.
            else:
                for bo in _ALLOWED_BYTEORDERS:
                    # Return cursor to first byte.
                    binary_in.seek(0)
                    header = np.fromfile(
                        binary_in, count=1, dtype=header_type.newbyteorder(bo))[0]
                    n_dims = header['dims']
                    print(f"{bo=}, {n_dims=}")
                    if n_dims in _ALLOWED_DIMS:
                        byteorder = bo
                        break
                else:
                    raise IOError(
                        f"Couldn't determine correct byteorder of file {fname}.")

            # Define dtypes.
            gas_type = np.dtype([('mass', '>f4'), ('r', '>f4', (n_dims,)), ('v', '>f4', (n_dims,)),
                                 ('rho', '>f4'), ('temp', '>f4'), ('hsmooth', '>f4'), ('metals', '>f4'), ('phi', '>f4')])
            dark_type = np.dtype([('mass', '>f4'), ('r', '>f4', (n_dims,)), ('v', '>f4', (n_dims,)),
                                  ('eps', '>f4'), ('phi', '>f4')])
            star_type = np.dtype([('mass', '>f4'), ('r', '>f4', (n_dims,)), ('v', '>f4', (n_dims,)),
                                  ('metals', '>f4'), ('tform', '>f4'), ('eps', '>f4'), ('phi', '>f4')])

            # Change byteorder of dtypes.
            gas_type = gas_type.newbyteorder(byteorder)
            dark_type = dark_type.newbyteorder(byteorder)
            star_type = star_type.newbyteorder(byteorder)

            # Load data
            gas = np.fromfile(binary_in, dtype=gas_type, count=header['n_gas'])
            dark = np.fromfile(binary_in, dtype=dark_type,
                               count=header['n_dark'])
            star = np.fromfile(binary_in, dtype=star_type,
                               count=header['n_star'])

            return cls(header, gas, dark, star)
