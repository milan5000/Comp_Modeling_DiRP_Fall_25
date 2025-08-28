import numpy as np



def main():
    pass



class Fluid:
    def __init__(self, rho, nx, ny, h):
        this.rho = rho # Density
        this.nx = nx + 2 # Nomber of cells, horizontal
        this.ny = ny + 2 # Number of cells, vertical
        this.nc = this.nx * this.ny # Number of cells
        this.h = h # Grid spacing
        this.u = np.zeros(this.nc) # Current velocity
        this.v = np.zeros(this.nc) # Current velocity
        this.u_new = np.zeros(this.nc) # Provisional velocity
        this.v_new = np.zeros(this.nc) # Provisional velocity
        this.p = np.zeros(this.nc) # Pressure
        this.s = np.zeros(this.nc) # Whether a cell is simulated (1) or not (0)
        this.m = np.ones(this.nc) # Smoke density
        this.m_new = np.zeros(this.nc) # Provisional smoke density
        this.n = nx * ny # NUMBER OF INTERIOR POINTS?
        
        def cell(i, j):
            return i * this.n + j
        
        def integrate(dt, g):
            """
            Apply gravity to the velocity field.
            """
            for i in range(1, this.nx):
                for j in range(1, this.ny - 1):
                    if this.s[cell(i, j)] != 0 and this.s[cell(i, j - 1)] != 0:
                        this.v[cell(i, j)] += g * dt
        
        def solve_incompressibility(n_it, dt):
            cp = this.rho * this.h / dt
            for i in range(1, this.nx - 1):
                for j in range(1, this.ny - 1):
                    if this.s[cell(i, j)] == 0:
                        continue
        
        def extrapolate():
            pass
        
        def sample_field(x, y, field):
            pass
        
        def avg_u(i, j):
            pass
        
        def avg_v(i, j):
            pass
        
        def advect_vel(dt):
            pass
        
        def advect_smoke(dt):
            pass



if __name__ == '__main__':
    main()