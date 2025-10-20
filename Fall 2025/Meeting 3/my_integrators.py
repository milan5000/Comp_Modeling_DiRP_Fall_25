import numpy as np

def ode_integrator(method: str, f, tspan: tuple, x0, dt: float):
    """Integrate a system of ODE's using the forward Euler method.
    
    Arguments:
    method: 'explicit_euler', 'explicit_rk2', or 'explicit_rk4'
    f: a scalar- or vector-valued differential equation in the form f(t, x)
    tspan: a tuple of (t0, tf)
    x0: the value at the initial time
    dt: the time step
    
    Returns:
    A tuple of time steps and corresponding solution vectors.
    
    Note: this implementation is not necessarily recommended for large systems.
    """
    t = tspan[0]
    x = x0
    ts = [tspan[0]] # Might be prudent to pre-allocate these arrays
    xs = [x0]
    while t < tspan[1]:
        if method == 'explicit_euler':
            x = explicit_euler_step(f, x, t, dt)
        elif method == 'explicit_rk2':
            x = explicit_rk2_step(f, x, t, dt)
        elif method == 'explicit_rk4':
            x = explicit_rk4_step(f, x, t, dt)
        else:
            raise Exception(f'{method} is not defined within my_integrators!')
        t += ???
        ts += ???
        xs += ???
    return (ts, xs)
    
    
def explicit_euler_step(f, xn, tn: float, dt: float):
    """Apply the Forward Euler integration method for one step.
    
    Arguments:
    f: a scalar- or vector-valued differential equation in the form f(t, x)
    xn: the value of the dependent variable(s) at the current step
    tn: the value of the independent variable at the current step
    dt: the step size
    
    Returns:
    The dependent variable(s) at the next step.
    """
    return ???
    
def explicit_rk2_step(f, xn, tn: float, dt: float):
    """Apply the Runge-Kutta 2 integration method for one step.
    
    Arguments:
    f: a scalar- or vector-valued differential equation in the form f(t, x)
    xn: the value of the dependent variable(s) at the current step
    tn: the value of the independent variable at the current step
    dt: the step size
    
    Returns:
    The dependent variable(s) at the next step.
    """
    # This is just the midpoint method!
    k1 = ???
    k2 = ???
    return ???

def explicit_rk4_step(f, xn, tn: float, dt: float):
    """Apply the Runge-Kutta 4 integration method for one step.
    
    Arguments:
    f: a scalar- or vector-valued differential equation in the form f(t, x)
    xn: the value of the dependent variable(s) at the current step
    tn: the value of the independent variable at the current step
    dt: the step size
    
    Returns:
    The dependent variable(s) at the next step.
    """
    k1 = ???
    k2 = ???
    k3 = ???
    k4 = ???
    return ???