import numpy as np

def ode_integrator(method: str, f, tspan: tuple, x0: np.ndarray, dt: float):
    """Integrate a system of ODE's using the forward Euler method.
    
    Arguments:
    f: a scalar- or vector-valued differential equation in the form f(t, x)
    tspan: a tuple of (t0, tf)
    x0: the value at the initial time
    dt: the time step
    
    Returns:
    A tuple of time steps and corresponding solution vectors.
    
    Note: this is not necessarily recommended for very large systems.
    """
    t = tspan[0]
    x = x0
    ts = [tspan[0]] # Might be prudent to pre-allocate these arrays
    xs = [x0]
    while t < tspan[1]:
        if method == 'euler_step':
            x = euler_step(f, x, t, dt)
        else if method == 'rk2_step':
            x = rk2_step(f, x, t, dt)
        else if method == 'rk4_step':
            x = rk4_step(f, x, t, dt)
        else:
            raise Exception(f'{method} is not defined within my_integrators!')
        t += dt
        ts += [t]
        xs += [x]
    return (ts, xs)
    
    
def euler_step(f, xn, tn: float, dt: float):
    """Apply the Forward Euler method for one time step."""
    return xn + dt * f(tn, xn)
    
def rk2_step(f, xn, tn: float, dt: float):
    """Apply the Runge-Kutta 2 method for one time step."""
    # This is just the midpoint method!
    k1 = f(tn, xn)
    k2 = f(tn + dt / 2, xn + dt * k1 / 2)
    return xn + dt * k2

def rk4_step(f, xn, tn: float, dt: float):
    """Apply the Runge-Kutta 4 method for one time step."""
    k1 = f(tn, xn)
    k2 = f(tn + dt / 2, xn + dt * k1 / 2)
    k3 = f(tn + dt / 2, xn + dt * k3 / 2)
    k4 = f(tn + dt, xn + dt * k3)
    return xn + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)