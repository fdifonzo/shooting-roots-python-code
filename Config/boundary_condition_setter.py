from math import sin, pi


def boundary_condition_setter(t, T, soil_parameters, bc_type):
    if bc_type == 'Ex1':
        top = soil_parameters.theta_top * (2 * T - t) / (2 * T)
        bottom = soil_parameters.theta_bottom
    elif bc_type == 'Ex2':
        top = -0.1 * sin(4 * pi * t / T) + soil_parameters.theta_top
        bottom = soil_parameters.theta_bottom
    elif bc_type == 'Ex3':
        top = 0.1 * sin(4 * pi * t / T) + soil_parameters.theta_top
        val = (soil_parameters.theta_top + soil_parameters.theta_bottom) / 4
        if t <= T / 4:
            bottom = val
        else:
            bottom = val + 0.02 * (t - T / 4 + 1) * (1 + sin(8 * pi * t / T))

    return top, bottom
