from Utils.from_theta_to_psi import *
from Utils.from_psi_to_theta import *
from math import exp, sqrt


def uptake_R(x_theta, soil_parameters, active_uptake, uptake_type):
    alpha = 0
    if active_uptake:
        x_psi = from_theta_to_psi(x_theta, soil_parameters)
        if uptake_type == 'Feddes':
            if soil_parameters.h[0] <= x_psi < soil_parameters.h[1]:
                alpha = (x_psi - soil_parameters.h[0]) / (soil_parameters.h[1] - soil_parameters.h[0])
            elif soil_parameters.h[1] <= x_psi <= soil_parameters.h[2]:
                alpha = 1
            elif soil_parameters.h[2] <= x_psi <= soil_parameters.h[3]:
                alpha = (x_psi - soil_parameters.h[3]) / (soil_parameters.h[2] - soil_parameters.h[3])

            alpha *= 0.1 / soil_parameters.Z  # 0.1 mm-1/d is T_pot on Potato Research

        elif uptake_type == 'Li':
            Tp = 0.64
            if soil_parameters.h[1] <= x_psi <= 0:
                alpha = 1 / (1 + exp(12.254 * (0.504 - (soil_parameters.theta_S - x_theta) / (soil_parameters.theta_S - from_psi_to_theta(soil_parameters.h[1], soil_parameters)))))
            elif soil_parameters.h[0] < x_psi < soil_parameters.h[1]:
                Theta = (x_theta - from_psi_to_theta(soil_parameters.h[0], soil_parameters)) / (from_psi_to_theta(soil_parameters.h[1], soil_parameters) - from_psi_to_theta(soil_parameters.h[0], soil_parameters))
                Psi = (x_psi - soil_parameters.h[0]) / (soil_parameters.h[1] - soil_parameters.h[0])
                alpha = min(1, sqrt(Theta * Psi) / (Tp / soil_parameters.Tm))
            elif x_psi <= soil_parameters.h[0]:
                alpha = 1

            alpha *= 0.1 / soil_parameters.Z

    return alpha
