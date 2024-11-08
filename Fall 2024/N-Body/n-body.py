import json
from my_integrators import (
    ode_integrator,
    explicit_euler_step,
    explicit_rk2_step,
    explicit_rk4_step
)
import numpy as np
from pathlib import Path
import sys



def main():
    # Read in problem parameters
    path = Path(sys.argv[1]) if (len(sys.argv) > 1) else Path("")
    params_file = open(path / 'params.json')
    params = json.load(params_file)
    params_file.close()
    G = params['G']
    ta = params['ta']
    tb = params['tb']
    dt = params['dt']
    
    # Read in initial conditions
    # Format is m r1 r2 r3 v1 v2 v3
    ms = [] # Hold masses
    u = [] # Solution vector
    nb = 0 # Number of bodies
    initial_file = open(path / '0')
    for line in initial_file:
        line = [int(item) for item in line.split()]
        ms.append(line[0])
        u += line[1:7]
        nb += 1
    initial_file.close()
    
    def f(t, u):
        # For i in len/6
        # Apply gravitational forces from EVERY OTHER BODY to this
        # Or is there a more effiecient way to do this...?
        # What expression do I subtract?
        # ???
        # ???
        # ???
        return 0
    
    # Solve
    # For small case: solve all at once, then write to file
    # For big case: write each time step (or not)
    n = 0
    t = ta
    while t < tb:
        n += 1
        t += dt
        
        # Calculate step
        # u = ???
        
        # Write to case file
        output_file = open(path / f'{n}')
        for i in range(nb)
            data = u[(6 * i):(7 * i)]
            for j in range(6):
                if j < 5:
                    output_file.write(f'{u[6 * i + j]} ')
                elif i < nb - 1:
                    output_file.write(f'{u[6 * i + j]}\n')
                else:
                    output_file.write(f'{u[6 * i + j]}')
        output_file.close()
    
    # That's it!
    # Notice that postprocessing is being offloaded elsewhere!



if __name__ == '__main__':
    main()