from collections import deque
import sys
import numpy as np
import math
sys.path.append('../')

if __name__ == "__main__":
    import sys
    print("initial_program.py executed directly")


################################
## MUTABLE FUNCTION ############
################################  

def guess_sequence():

    # EVOLVE-BLOCK-START
    out = lambda x: x+5
    # EVOLVE-BLOCK-END

    return out


