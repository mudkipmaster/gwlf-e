import numpy as np
from Timer import time_function
from InitGrN import InitGrN


def GrazingN(PctGrazing,GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN):
    result = np.zeros((12,))
    init_gr_n = InitGrN(GrazingAnimal,NumAnimals,AvgAnimalWt,AnimalDailyN)
    for i in range(12):
        result[i] = PctGrazing[i] * (init_gr_n / 12)
    return result


def GrazingN_2(PctGrazing, InitGrN):
    return PctGrazing * (InitGrN / 12)