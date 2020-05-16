from Utils.from_theta_to_mu import *
from .boundary_condition_setter import *
from numpy import zeros


def guess_sol(t, z, T, soil_parameters, bc_type):
    theta_top, theta_bottom = boundary_condition_setter(t, T, soil_parameters, bc_type)
    len_z = len(z)
    out = zeros(len_z)
    for i in range(len_z):
        out[i] = from_theta_to_mu(theta_top + z[i] * (theta_bottom - theta_top) / soil_parameters.Z, soil_parameters)

    return out
