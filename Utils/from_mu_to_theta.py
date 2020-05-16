import numpy as np


def from_mu_to_theta(mu, soil_parameters):
    theta = soil_parameters.theta_r + soil_parameters.lambda_ * mu * (soil_parameters.theta_S - soil_parameters.theta_r)
    len_mu = np.atleast_1d(mu).shape[0]
    if len_mu > 1:
        for i in range(mu.shape[0]):
            for j in range(mu.shape[1]):
                theta[i, j] = min(max(theta[i, j], soil_parameters.theta_r), soil_parameters.theta_S)

    return theta
