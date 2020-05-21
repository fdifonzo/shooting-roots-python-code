from Config.uptake_R import *
from Utils.from_mu_to_theta import *
import numpy as np


def model_fun(x, y, soil_parameters, dt, y_old, active_uptake, uptake_type):
    out = np.zeros(2)
    out[0] = y[1]
    out[1] = (soil_parameters.lambda_ * (soil_parameters.theta_S - soil_parameters.theta_r) / soil_parameters.K_S) * (
                y[0] - y_old) / dt + uptake_R(from_mu_to_theta(y[0], soil_parameters), soil_parameters, active_uptake,
                                              uptake_type) / soil_parameters.K_S + soil_parameters.lambda_ * y[1]

    return out
