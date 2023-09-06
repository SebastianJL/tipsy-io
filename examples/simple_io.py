# Needs to be run from within examples folder.

from tipsy_io import Tipsy
import numpy as np

# Load file.
t = Tipsy.fromfile("test_in.tipsy")

# t.gas, t.dark and t.star are just numpy arrays.
# Shuffle is inplace and therefore changes the Tipsy object.
np.random.shuffle(t.gas)
np.random.shuffle(t.dark)
np.random.shuffle(t.star)

# Save changed tipsy data to file.
t.tofile("test_out.tipsy")

# Access field in header. See README.md for more fields.
print(f"{t.header['n_dark'] = }")

# Access "columns" particle types.
print(f"{t.dark['v'] = }")
print(f"{t.gas['mass'] = }")
