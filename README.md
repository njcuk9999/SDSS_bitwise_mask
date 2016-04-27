# SDSS_bitwise_mask

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
