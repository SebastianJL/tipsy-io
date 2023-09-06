from tipsy_io import Tipsy
import numpy as np


def test_save_load_cycle(tmpdir):
    t = Tipsy.fromfile('tests/test_in.tipsy')
    outfile = tmpdir.join('test_out.tipsy')
    t.tofile(outfile)
    t_copy = t.fromfile(outfile)

    assert np.all(t.header == t_copy.header)
    assert np.all(t.gas == t_copy.gas)
    assert np.all(t.dark == t_copy.dark)
    assert np.all(t.star == t_copy.star)
