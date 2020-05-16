from numpy import zeros


def der_guess_sol(t, z, soil_parameters):
    len_z = len(z)
    out = zeros(len_z)
    for i in range(len_z):
        out[i] = (soil_parameters.theta_bottom - soil_parameters.theta_top) / soil_parameters.Z

    return out
