from Core.model_fun import model_fun
import numpy as np


def forward_spatial_integrator(z, con, soil_parameters, dt, dz, y_old, active_uptake, uptake_type):
    y = con
    for k in range(len(z) - 1):
        y_pred = y[k] + dz * model_fun(z[k], y[k], soil_parameters, dt, y_old[k], active_uptake, uptake_type)
        y_corr = y[k] + dz * model_fun(z[k + 1], y_pred, soil_parameters, dt, y_old[k], active_uptake, uptake_type).reshape(con.shape)
        y = np.append(y, y_corr, axis=0)

    return y
