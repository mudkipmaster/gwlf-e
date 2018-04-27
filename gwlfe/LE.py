import numpy as np
from Timer import time_function
from SedAFactor import SedAFactor
from StreamFlowVol import StreamFlowVol
from Memoization import memoize


@memoize
def LE(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow, CNP_0, Imper,
       ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0, RecessionCoef, SeepCoef
       , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow, StreamWithdrawal, GroundWithdrawal
       , NumAnimals, AvgAnimalWt, StreamFlowVolAdj, SedAFactor_0, AvKF, AvSlope, SedAAdjust):
    result = np.zeros((NYrs, 12))
    sedafactor = SedAFactor(NumAnimals, AvgAnimalWt, NRur, NUrb, CNI_0, CNP_0, CN, Imper, Area, SedAFactor_0, AvKF,
                            AvSlope, SedAAdjust)
    streamflowvol = StreamFlowVol(NYrs, DaysMonth, Temp, InitSnow_0, Prec, NRur, NUrb, Area, CNI_0, AntMoist_0, Grow,
                                  CNP_0, Imper,
                                  ISRR, ISRA, CN, UnsatStor_0, KV, PcntET, DayHrs, MaxWaterCap, SatStor_0,
                                  RecessionCoef, SeepCoef
                                  , Qretention, PctAreaInfil, n25b, Landuse, TileDrainDensity, PointFlow,
                                  StreamWithdrawal, GroundWithdrawal)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = sedafactor * (StreamFlowVolAdj * (streamflowvol[Y][i] ** 0.6))
    return result


def LE_2():
    pass