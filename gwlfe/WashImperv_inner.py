# from numba.pycc import CC
import numpy as np
import math

# cc = CC('WashImperv_inner_compiled')


@cc.export('WashImperv_inner',
           '(int64, int32[:,::1], float64[:,:,::1], int64, int64, float64[:,:,::1], float64[:,:,:,::1])')
def WashImperv_inner(NYrs, DaysMonth, Temp, NRur, nlu, water, qruni):
    result = np.zeros((NYrs, 12, 31, 16))
    impervaccum = np.zeros(16)
    carryover = np.zeros(16)
    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                for l in range(nlu):
                    impervaccum[l] = carryover[l]
                    impervaccum[l] = (impervaccum[l] * np.exp(-0.12) + (1 / 0.12) * (1 - np.exp(-0.12)))
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        for l in range(NRur, nlu):
                            result[Y][i][j][l] = (1 - math.exp(-1.81 * qruni[Y][i][j][l])) * impervaccum[l]
                            impervaccum[l] -= result[Y][i][j][l]
                else:
                    pass
                for l in range(nlu):
                    carryover[l] = impervaccum[l]
    return result
