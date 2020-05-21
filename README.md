# shooting-roots-python-code
Python code for shooting method applied to Richards' equation with root water uptake models. 

Please see F.V. Difonzo, C. Masciopinto, M. Vurro and M. Berardi, Shooting the numerical solution of moisture flow equation with root water uptake models, submitted to Journal of Hydrology, 2020.

Within this folder you find Python scripts developed in a Python 3.7 environment.

***
TO RUN an examples, go to the folder Examples and run the a .py script therein.
If you want to create your own example, please follow the same structure.
***

In the folder Config you find customizable .py scripts for running examples provided in Examples.
In particular, you could set:
 - boundary conditions (boundary_condition_setter.py)
 - derivative of initial guess for starting TMoL (der_guess_sol.py)
 - initial guess for starting TMoL (guess_sol.py)
 - spatial numerical integrator (forward_spatial_integrator.py)
 - uptake type (select_uptake_type.py)
 - set soil parameters (SoilParameters.py)
 - set uptake parameters (uptake_R.py)

The folder Utils contains .py scripts necessary for the Gardner constitutive relation setting 
and Kirchhoff transform used in the examples.

The folder Core contains the function to integrate (model_fun.py), and the class ShootingSol.py which provides 
the numerical solution. This folder should be NOT modified by the user.
