from typing import List, Tuple
import numpy as np
from dataclasses import dataclass, field

header_type = np.dtype([('time', '>f8'), ('n', '>i4'), ('dims', '>i4'),
                       ('n_gas', '>i4'), ('n_dark', '>i4'), ('n_star', '>i4'), ('pad', '>i4')])


@dataclass
class Tipsy:
    header: header_type
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
    def fromfile(cls, fname: str) -> "Tipsy":
        with open(fname, 'rb') as tipsy:
            header = np.fromfile(tipsy, dtype=header_type, count=1)[0]
            n_dims = header['dims']
            gas_type = np.dtype([('mass', '>f4'), ('r', '>f4', (n_dims,)), ('v', '>f4', (n_dims,)),
                                 ('rho', '>f4'), ('temp', '>f4'), ('hsmooth', '>f4'), ('metals', '>f4'), ('phi', '>f4')])
            dark_type = np.dtype([('mass', '>f4'), ('r', '>f4', (n_dims,)), ('v', '>f4', (n_dims,)),
                                  ('eps', '>f4'), ('phi', '>f4')])
            star_type = np.dtype([('mass', '>f4'), ('r', '>f4', (n_dims,)), ('v', '>f4', (n_dims,)),
                                  ('metals', '>f4'), ('tform', '>f4'), ('eps', '>f4'), ('phi', '>f4')])
            gas = np.fromfile(tipsy, dtype=gas_type, count=header['n_gas'])
            dark = np.fromfile(tipsy, dtype=dark_type,
                               count=header['n_dark'])
            star = np.fromfile(tipsy, dtype=star_type,
                               count=header['n_star'])
            return cls(header, gas, dark, star)
