import numpy as np
from Timer import time_function
from DailyArrayConverter import get_value_for_yesterday
from NLU import NLU
from Water import Water
from CNP import CNP
from Melt import Melt
from GrowFactor import GrowFactor
from AMC5 import AMC5


def CNumPerv(NYrs, DaysMonth, Temp, NRur, NUrb, CNP_0, InitSnow_0, Prec, Grow, AntMoist_0):
    nlu = NLU(NRur, NUrb)
    result = np.zeros((NYrs, 12, 31, nlu))
    cnp = CNP(NRur, NUrb, CNP_0)
    water = Water(NYrs, DaysMonth, InitSnow_0, Temp, Prec)
    melt = Melt(NYrs, DaysMonth, Temp, InitSnow_0, Prec)
    grow_factor = GrowFactor(Grow)
    amc5 = AMC5(NYrs, DaysMonth, Temp, Prec, InitSnow_0, AntMoist_0)

    for Y in range(NYrs):
        for i in range(12):
            for j in range(DaysMonth[Y][i]):
                if Temp[Y][i][j] > 0 and water[Y][i][j] > 0.01:
                    if water[Y][i][j] < 0.05:
                        pass
                    else:
                        for l in range(NRur, nlu):
                            if cnp[1][l] > 0:
                                if melt[Y][i][j] <= 0:
                                    if grow_factor[i] > 0:
                                        # Growing season
                                        if get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) >= 5.33:
                                            result[Y][i][j][l] = cnp[2][l]
                                        elif get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) < 3.56:
                                            result[Y][i][j][l] = cnp[0][l] + (
                                                    cnp[1][l] - cnp[0][l]) * \
                                                                 get_value_for_yesterday(amc5, 0, Y, i, j, NYrs,
                                                                                         DaysMonth) / 3.56
                                        else:
                                            result[Y][i][j][l] = cnp[1][l] + (cnp[2][l] - cnp[1][l]) * (
                                                    get_value_for_yesterday(amc5, 0, Y, i, j, NYrs,
                                                                            DaysMonth) - 3.56) / 1.77
                                    else:
                                        # Dormant season
                                        if get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) >= 2.79:
                                            result[Y][i][j][l] = cnp[2][l]
                                        elif get_value_for_yesterday(amc5, 0, Y, i, j, NYrs, DaysMonth) < 1.27:
                                            result[Y][i][j][l] = cnp[0][l] + (
                                                    cnp[1][l] - cnp[0][l]) * \
                                                                 get_value_for_yesterday(amc5, 0, Y, i, j, NYrs,
                                                                                         DaysMonth) / 1.27
                                        else:
                                            result[Y][i][j][l] = cnp[1][l] + (cnp[2][l] - cnp[1][l]) * (
                                                    get_value_for_yesterday(amc5, 0, Y, i, j, NYrs,
                                                                            DaysMonth) - 1.27) / 1.52
                                else:
                                    result[Y][i][j][l] = cnp[2][l]
    return result


def CNumPerv_2():
    pass