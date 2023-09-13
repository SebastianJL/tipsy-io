# Needs to be run from the project root.

from tipsy_io import Tipsy
import numpy as np

# Load file.
t = Tipsy.fromfile("examples/test_in.tipsy")

# t.gas, t.dark and t.star are just numpy arrays.
# Shuffle is inplace and therefore changes the Tipsy object.
np.random.shuffle(t.gas)
np.random.shuffle(t.dark)
np.random.shuffle(t.star)

# Save changed tipsy data to file.
t.tofile("examples/test_out.tipsy")

# Access field in header. See README.md for more fields.
print(f"{t.header['n_dark'] = }")

# Access speed of all dark particles.
print(f"{t.dark['v'] = }")

# Access mass of all gas particles.
print(f"{t.gas['mass'] = }")
