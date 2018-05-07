import numpy as np
from Timer import time_function
from NLU import NLU
from Memoization import memoize


@memoize
def UrbAreaTotal(NRur,NUrb,Area):
    result = 0
    nlu = NLU(NRur,NUrb)
    for l in range(NRur, nlu):
        result += Area[l]
    return result

# @time_function
def UrbAreaTotal_2(NRur,NUrb,Area):
    nlu = NLU(NRur, NUrb)
    return np.sum(Area[NRur:nlu])