from math import exp


def from_psi_to_theta(psi, soil_parameters):
    return soil_parameters.theta_r + (soil_parameters.theta_S - soil_parameters.theta_r) * exp(
        soil_parameters.lambda_ * psi)
