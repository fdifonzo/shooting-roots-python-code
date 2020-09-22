# Python code architecture
Here an analytical description of the architecture of Python code is presented, for sake of the reproducibility by the interested reader. 
Our Python code is structured as follows: 
- the folder named *Core* contains the class *ShootingSol.py* and the method *model_fun.py*. More specifically, the class *ShootingSol.py* contains the class of the shooting solution, whose properties are: 	
	- step-sizes \Delta t, \Delta z; 
	- solution intervals for time and space; 
	- tolerance for convergence of the shooting algorithm (based on secant method);
	- temporal and spatial integration intervals; 
	- vectors of solution and its spatial derivative;	
	
  moreover, it contains the shooting algorithm itself which actually computes the numerical solution. 
  The method *model_fun.py* implements (13) in the paper. 
	These codes should **NOT** be modified by the user;

- the folder named *Utils* provides the conversion functions to switch from \theta to \mu representation and vice-versa, and from \psi to \mu representation and vice-versa. 
	
	These methods should **NOT** be modified by the user;
	
- the folder named *Config* contains the following methods:	
	- *boundary_condition_setter.py*: it allows the user to set her/his own top and bottom boundary conditions;
	- *der_guess_sol.py*: it allows the user to set a guess for the spatial derivative of the initial condition at t=0;
	- *forward_spatial_integrator.py*: it allows the user to implement her/his own desired numerical integrator for solving the problem of interest;
	- *guess_sol.py*: it allows the user to set a guess for the initial condition at time t=0;
	- *select_uptake_type.py*: it has to be enriched with the uptake type required for the given problem;
	- *SoilParameters.py*: it is a class which contains all the information about the soil used in the given problem, and should be enriched appropriately;
	- *uptake_R.py*: it implements the uptake model to be used in the experimental simulation, and has to be modified accordingly to the types listed within *select_uptake_type.py*.

	These methods are written is such a way that the user can modify the folder content as specified within each method, so to appropriately model the desired problem and run the algorithm to solve it.

- the folder named *Examples* contains the main programs: here, the user has to create her/his own main program, specifying all the required parameters in order to select the correct inputs from the *Config* folder (previously customized) and run the algorithm, which would provide a table with the soil parameters used and a graphical representation of the simulation result.
