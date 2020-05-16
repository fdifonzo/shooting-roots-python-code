def from_theta_to_mu(theta, soil_parameters):
    return (theta - soil_parameters.theta_r) / (
                soil_parameters.lambda_ * (soil_parameters.theta_S - soil_parameters.theta_r))
