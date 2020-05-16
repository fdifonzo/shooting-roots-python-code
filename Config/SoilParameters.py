import numpy as np


class SoilParameters:
    def __init__(self):
        self.lambda_ = 0  # Gardner hydraulic parameter; see Li et al. 20
        self.theta_r = 0
        self.theta_S = 0
        self.theta_top = 0
        self.theta_bottom = 0
        self.K_S = 0
        self.h = []
        self.Tm = 0
        self.Z = 0

    def get_soil_parameters(self, ind, active_uptake, uptake_type):
        self.lambda_ = 0.1
        if ind == 0:
            self.theta_r = 0.0650
            self.theta_S = 0.45
            self.theta_top = 0.1 * self.theta_r + 0.9 * self.theta_S
            self.theta_bottom = 0.9 * self.theta_r + 0.1 * self.theta_S
            self.K_S = 299.5
            self.Z = 30
            if active_uptake:
                if uptake_type == 'Feddes':
                    self.h = np.array([-16000, -500, -25, -10])
                elif uptake_type == 'Li':
                    self.h = np.array([-16000, -200])
                    self.Tm = 0.63
        elif ind == 1:
            self.theta_r = 0
            self.theta_S = 0.48
            self.theta_top = 0.5 * self.theta_r + 0.5 * self.theta_S
            self.theta_bottom = 0.9 * self.theta_r + 0.1 * self.theta_S
            self.K_S = 175.4
            self.Z = 25
            if active_uptake:
                if uptake_type == 'Feddes':
                    self.h = np.array([-16000, -500, -25, -10])
                elif uptake_type == 'Li':
                    self.h = np.array([-16000, -300])
                    self.Tm = 0.61
