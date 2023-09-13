from tipsy_io import Tipsy
import numpy as np
import pytest


def test_save_load_cycle(tmpdir):
    t = Tipsy.fromfile('tests/test_in_be.tipsy')
    outfile = tmpdir.join('test_out.tipsy')
    t.tofile(outfile)
    t_copy = t.fromfile(outfile)

    assert np.all(t.header == t_copy.header)
    assert np.all(t.gas == t_copy.gas)
    assert np.all(t.dark == t_copy.dark)
    assert np.all(t.star == t_copy.star)


def test_load_big_endian_auto():
    t = Tipsy.fromfile('tests/test_in_be.tipsy')


def test_load_little_endian_auto():
    t = Tipsy.fromfile('tests/test_in_le.tipsy')


def test_load_correct_byteorder():
    t = Tipsy.fromfile('tests/test_in_be.tipsy', byteorder='>')


def test_load_wrong_byteorder():
    with pytest.raises(IOError, match=r"Couldn't open file with byteorder"):
        t = Tipsy.fromfile('tests/test_in_be.tipsy', byteorder='<')


def test_load_invalid_byteorder():
    with pytest.raises(KeyError, match=r"byteorder must be one of (.+) or None"):
        t = Tipsy.fromfile('tests/test_in_be.tipsy', byteorder=',')
