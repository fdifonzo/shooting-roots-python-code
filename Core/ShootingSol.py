from Config.guess_sol import *
from Config.der_guess_sol import *
from Config.forward_spatial_integrator import *
from Utils.from_mu_to_theta import *
import numpy as np


class ShootingSol:
    def __init__(self, dt, dz, t_interval, z_interval, tol):
        self.dt = dt
        self.dz = dz
        self.tInterval = t_interval
        self.zInterval = z_interval
        self.absTol = tol
        self.t_sol = []
        self.z_sol = []
        self.f_sol = []
        self.der_f_sol = []

    def shooting_method(self, soil_parameters, active_uptake, uptake_type, bc_type):
        Z0 = self.zInterval[0]
        Z = self.zInterval[1]
        T0 = self.tInterval[0]
        T = self.tInterval[1]
        Nt = int((T - T0) / self.dt)
        Nz = int((Z - Z0) / self.dz)
        t_span = np.linspace(T0, T, num=Nt)

        self.t_sol = np.linspace(T0, T * 24, num=Nt)
        self.z_sol = np.linspace(Z0, Z, num=Nz)
        mu_init = guess_sol(T0, self.z_sol, T, soil_parameters, bc_type)
        dmudz_init = der_guess_sol(T, self.z_sol, soil_parameters)

        y_old = mu_init
        f_sol = y_old
        der_f_sol = dmudz_init

        for i in range(1, Nt):
            con_1 = guess_sol(t_span[i], [Z0], T, soil_parameters, bc_type)
            con_2 = guess_sol(t_span[i], [Z], T, soil_parameters, bc_type)
            diff = der_guess_sol(t_span[i], [0], soil_parameters)
            shoot1 = diff - 2
            shoot2 = diff + 2
            ic1 = np.array([con_1, shoot1]).reshape(1, 2)
            ic2 = np.array([con_1, shoot2]).reshape(1, 2)
            sol1 = forward_spatial_integrator(self.z_sol, ic1, soil_parameters, self.dt, self.dz, y_old, active_uptake, uptake_type)
            sol2 = forward_spatial_integrator(self.z_sol, ic2, soil_parameters, self.dt, self.dz, y_old, active_uptake, uptake_type)
            sol1 = sol1[-1, 0] - con_2
            sol2 = sol2[-1, 0] - con_2
            sol3 = sol1
            while abs(np.real(sol3)) > self.absTol:
                shoot3 = shoot2 - sol2 * (shoot2 - shoot1) / (sol2 - sol1)
                ic3 = np.array([con_1, shoot3]).reshape(1, 2)
                sol3 = forward_spatial_integrator(self.z_sol, ic3, soil_parameters, self.dt, self.dz, y_old, active_uptake,
                                   uptake_type)
                y = sol3
                sol3 = sol3[-1, 0] - con_2
                shoot1 = shoot2
                shoot2 = shoot3
                sol1 = sol2
                sol2 = sol3

            y_old = y[:, 0]
            f_sol = np.append(f_sol, y_old).reshape(i + 1, mu_init.size)
            der_f_sol = np.append(der_f_sol, y[:, 1]).reshape(i + 1, mu_init.size)

        self.f_sol = from_mu_to_theta(f_sol, soil_parameters)
        self.der_f_sol = from_mu_to_theta(der_f_sol, soil_parameters)
