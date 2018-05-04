import numpy as np
from gwlfe.AFOS.GrazingAnimals.Loads.GrazingN import GrazingN
from gwlfe.AFOS.GrazingAnimals.Loads.InitGrN import InitGrN


def GRAccManAppN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN, GRPctManApp, PctGrazing):
    result = np.zeros((12,))
    grazing_n = GrazingN(PctGrazing, GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    init_gr_n = InitGrN(GrazingAnimal_0, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for i in range(12):
        result[i] = (result[i] + (init_gr_n / 12) - (GRPctManApp[i] * init_gr_n) - grazing_n[i])
        if result[i] < 0:
            result[i] = 0
    return result


def GRAccManAppN_2(_InitGrN, GRPctManApp, GrazingN):
    init_gr_n = InitGrN()
    result = (np.repeat(InitGrN / 12, 12)) - (GRPctManApp * np.repeat(InitGrN, 12)) - GrazingN
    result = np.maximum(result, 0)
    return result