# TipsyIO
Read and write tipsy files as numpy arrays. Tipsy a binary data format used in PKDGRAV3.

# Basic usage
See examples folder for basic examples.


## Tipsy file format
### Header
| field name:  | time | n   | dims               | n_gas              | n_dark                      | n_star               | pad |
|--------------|------|-----|--------------------|--------------------|-----------------------------|----------------------|-----|
| dtype:       | f8   | i4  | i4                 | i4                 | i4                          | i4                   | i4  |
| explanation: | ???  | ??? | Spatial dimensions | # of gas particles | # of  dark matter particles | # of  star particles | ??? |

### Body
n_gas + n_dark + n_star particles in the format

#### gas particles
| field name:  | mass | r          | v          | rho | temp | hsmooth | metals | phi |
|--------------|------|------------|------------|-----|------|---------|--------|-----|
| dtype:       | f4   | {f4, dims} | {f4, dims} | f4  | f4   | f4      | f4     | f4  |
| explanation: | Mass | Position   | Velocity   | ??? | ???  | ???     | ???    | ??? |

#### dark particles
| field name:  | mass | r          | v          | eps | phi |
|--------------|------|------------|------------|-----|-----|
| dtype:       | f4   | {f4, dims} | {f4, dims} | f4  | f4  |
| explanation: | Mass | Position   | Velocity   | ??? | ??? |

#### star particles
| field name:  | mass | r          | v          | metals | tform | eps | phi |
|--------------|------|------------|------------|--------|-------|-----|-----|
| dtype:       | f4   | {f4, dims} | {f4, dims} | f4     | f4    | f4  | f4  |
| explanation: | Mass | Position   | Velocity   | ???    | ???   | ??? | ??? |
