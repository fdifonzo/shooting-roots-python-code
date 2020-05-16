import math as m


def from_theta_to_psi(theta, soil_parameters):
    if theta <= soil_parameters.theta_r:
        psi = -m.inf
    else:
        psi = m.log((theta - soil_parameters.theta_r) / (soil_parameters.theta_S - soil_parameters.theta_r)) / soil_parameters.lambda_

    return psi
