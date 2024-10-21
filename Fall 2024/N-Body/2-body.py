import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from my_integrators import ode_integrator
from scipy.integrate import solve_ivp

def main():
    # Define parameters
    # If I knew Jupyter notebook well, it would come in handy here. This is a
    # relatively lightweight case, where we just want to get a feel fot the
    # ODE. Interactive computing is great for fiddling around -- fine-tuning
    # parameters and setting up quick plots.
    mu = 1 # Gravitational parameter G*M
    r0 = 1 # Initial distance
    vesc = (2 * mu / r0) ** 0.5
    u0 = np.array([r0, 0, 0, vesc - 0.1]) # Initial state
    t0 = 0
    tf = 1000
    dt = 0.1
    
    
    def f(t, u):
        r3 = np.dot(u[0:2], u[0:2]) ** 1.5 + 0.0000001 # Careful slicing!
        #print(r3)
        return np.array([u[2], u[3], -mu / r3 * u[0], -mu / r3 * u[1]])
    # print(f(0, u0))
    
    # In-house function
    # Show how help() can be used with the Python shell
    (ts, us) = ode_integrator('explicit_rk4', f, (t0, tf), u0, dt)
    
    # Scipy function
    #sol = solve_ivp(f, (t0, tf), u0)
    
    # Plot position
    fig, ax = plt.subplots()
    ax.scatter(0, 0)
    ax.plot([u[0] for u in us], [u[1] for u in us], label='RK4')
    # ax.plot(sol.y[0, :], sol.y[1, :], label='SciPy')
    ax.legend()
    plt.show()
    
    # Is energy conserved?
    ks = np.array([0.5 * np.dot(u[2:4], u[2:4]) for u in us])
    ugs = np.array([-mu / np.linalg.norm(u[0:2]) for u in us])

    fig, axs = plt.subplots(2)
    axs[0].plot(ts, ks, label='Kinetic Energy per Unit Mass')
    axs[0].plot(ts, ugs, label='Potential Energy per Unit Mass')
    axs[0].legend()
    axs[1].plot(ts, ks + ugs, label='Total Energy per Unit Mass')
    axs[1].legend()
    plt.show()
    
    # What about momentum?



if __name__ == '__main__':
    main()