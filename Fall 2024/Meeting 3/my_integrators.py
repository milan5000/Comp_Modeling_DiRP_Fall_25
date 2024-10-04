import numpy as np

def ode_integrator(method: str, f, tspan: tuple, y0: np.ndarray, dt: float):
    """Integrate a system of ODE's using the forward Euler method.
    
    Arguments:
    f: a scalar- or vector-valued differential equation in the form f(t, x)
    tspan: a tuple of (t0, tf)
    y0: the value at the initial time
    dt: the time step
    """
    return 0
    
    
def euler_step(f, xn, tn: float, dt: float):
    """Apply the Forward Euler method for one time step."""
    return xn + dt * f(tn, xn)
    
def rk2_step(f, xn, tn: float, dt: float):
    # This is just the midpoint method!
    return 0

def rk4_step(f, xn, tn: float, dt: float):
    k1 = f(tn, xn)
    k2 = f(tn + dt / 2, xn + dt * k1 / 2)
    k3 = f(tn + dt / 2, xn + dt * k3 / 2)
    k4 = f(tn + dt, xn + dt * k3)
    return xn + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)