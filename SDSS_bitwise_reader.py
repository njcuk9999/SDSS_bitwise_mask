"""
Description of program
"""
from astropy.table import Table as table
import numpy as np

# ==============================================================================
# Define variables
# ==============================================================================
# define constants (for example run)
workspace = './'
dpath = workspace + 'input_catalogue.fits'
spath = workspace + 'output_catalogue.fits'
flagcol = 'sdss_flags'


# ==============================================================================
# Define functions
# ==============================================================================
def sdss_bitwise(mode='hex'):
    """
    Reads sdss_bitmasks.txt and uses this to locate information on the
    SDSS bitwise flats.

    All data from here:
        https://www.sdss3.org/dr10/algorithms/bitmask_flags1.php
        https://www.sdss3.org/dr10/algorithms/bitmask_flags2.php

    :param mode: string, output required
                     if "hex" returns the hex codes
                     if "num" return the numerical number
                     if "desc" returns a description of the column
    :return:
    """
    # define constants
    filename = './sdss_bitmasks.txt'

    # open file and read lines
    f = open(filename, 'r')
    lines = f.readlines()

    # define storage dictionaries
    dhex, dnum, ddesc, raw = {}, {}, {}, {}

    # loop round lines and add to dictionaries
    for line in lines:
        bname, H, desc = (line.replace('\n', '')).split('\t')
        I = int(H, 16)
        dhex[bname], dnum[bname], ddesc[bname] = [hex(I), I, desc]
    if mode == 'hex':
        return dhex
    elif mode == 'num' or mode == 'int':
        return dnum
    elif mode == 'desc':
        return ddesc
    else:
        return raw


# ==============================================================================
# Start of code
# ==============================================================================
if __name__ == '__main__':
    # load data
    print "\n Reading data..."
    data = table.read(dpath)
    # load flag column
    flags = data[flagcol]
    # get sdss bitwise
    print "\n Getting bitwise data..."
    bitwise = sdss_bitwise("hex")
    # loop round each bitwise and create new column in data
    for name in bitwise:
        if name == 'RESERVED':
            continue
        print "\n Processing bitwise flag: " + str(name) + "..."
        mask = (flags & int(bitwise[name], 16)) == int(bitwise[name], 16)
        data[name] = np.array(mask, dtype=bool)
    # write data to new file
    print "\n Writing data to " + spath
    data.write(spath, overwrite=True)

# ==============================================================================
# End of code
# ==============================================================================
