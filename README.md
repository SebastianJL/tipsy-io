# TipsyIO
Read and write tipsy files as numpy arrays. Tipsy is a binary data format used in [PKDGRAV3][pkdgrav3].

# Basic usage
See [examples folder](examples).


## Tipsy file format
### Header
| field name:  | time                                                                                                | n                     | dims                           | n_gas              | n_dark                      | n_star               | pad                                                                            |
|--------------|-----------------------------------------------------------------------------------------------------|-----------------------|--------------------------------|--------------------|-----------------------------|----------------------|--------------------------------------------------------------------------------|
| dtype:       | f8                                                                                                  | i4                    | i4                             | i4                 | i4                          | i4                   | i4                                                                             |
| explanation: | Usually expansion factor for cosmology simulations, or time in pkdgrav3 units for non-cosmological simulations. | n_gas +n_dark +n_star | Spatial dimensions, 1, 2 or 3. | # of gas particles | # of  dark matter particles | # of  star particles | 4 byte padding in case header is a struct that needs to be aligned to 8 bytes. |

### Body
n_gas + n_dark + n_star particles in the format

#### gas particles
| field name:  | mass | r          | v          | rho     | temp        | hsmooth          | metals                      | phi                     |
|--------------|------|------------|------------|---------|-------------|------------------|-----------------------------|-------------------------|
| dtype:       | f4   | {f4, dims} | {f4, dims} | f4      | f4          | f4               | f4                          | f4                      |
| explanation: | Mass | Position   | Velocity   | Density | Temperature | Smoothing length | Metalicity of the particle. | Gravitational potential |

#### dark particles
| field name:  | mass | r          | v          | eps              | phi                     |
|--------------|------|------------|------------|------------------|-------------------------|
| dtype:       | f4   | {f4, dims} | {f4, dims} | f4               | f4                      |
| explanation: | Mass | Position   | Velocity   | Softening length | Gravitational potential |

#### star particles
| field name:  | mass | r          | v          | metals     | tform                      | eps              | phi                     |
|--------------|------|------------|------------|------------|----------------------------|------------------|-------------------------|
| dtype:       | f4   | {f4, dims} | {f4, dims} | f4         | f4                         | f4               | f4                      |
| explanation: | Mass | Position   | Velocity   | Metalicity | Time when star was formed. | Softening length | Gravitational potential |

The tipsy file can either be saved in big or little endian format. This is tested by reading the header and checking if the dims is equal to 1, 2 or 3.

[pkdgrav3]: <https://bitbucket.org/dpotter/pkdgrav3/src/master/> "pkdgrav website"
