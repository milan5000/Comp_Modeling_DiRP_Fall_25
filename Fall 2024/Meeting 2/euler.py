import numpy as np
from matplotlib import pyplot as plt



def main():
    # Part 1: Stability
    fig, ax = plt.subplots()
    
    params = {
        'alpha': 1,
        't0': 0,
        'tf': 10,
        'dt': 1,
        'x0': 5,
        'f': lambda x, t, params : -params['alpha'] * x,
        'exact': lambda t, params : params['x0'] * np.exp(-params['alpha'] * t)
    }
    
    dts = [2.5, 2, 1, 0.5]
    for dt in dts:
        params['dt'] = dt
        ts, xs = test_case(params)
        ax.plot(ts, xs, label=f"dt={dt}")
    ts = np.linspace(params['t0'], params['tf'], 10001)
    xs = params['exact'](ts, params)
    ax.plot(ts, xs, label='exact')
    ax.set_title('Forward Euler Stability')
    ax.set_xlabel('t')
    ax.set_ylabel('x')
    ax.legend()
    plt.show()
    
    # Part 2: Accuracy
    # Demonstrating that forward finite difference is O(h) accurate
    dts = [0.8, 0.4, 0.2, 0.1, 0.05, 0.025, 0.0125, 0.00625, 0.003125]
    invdts = []
    es = []
    for dt in dts:
        params['dt'] = dt
        ts, xs = test_case(params)
        invdts += [1 / dt]
        es += [abs(xs[-1] - params['exact'](params['tf'], params))]
        ##es += [sum([e]) ** 0.5]
    fig, ax = plt.subplots()
    ax.loglog(invdts, es, label='Error')
    hs = [0.0125, 0.00625, 0.003125]
    invhs = [1 / h for h in hs]
    ax.loglog(invhs, [0.001 * h for h in hs], label='O(h)')
    ax.loglog(invhs, [0.001 * h**2 for h in hs], label='O(h^2)')
    ax.loglog(invhs, [0.001 * h**3 for h in hs], label='O(h^3)')
    ax.set_title('Forward Euler Accuracy\nConsidering error at x(tf)')
    ax.set_xlabel('Inverse Time Step 1/dt')
    ax.set_ylabel('Error Magnitude')
    ax.legend()
    plt.show()



def test_case(params: dict):
    """Apply the Forward Euler method to one case.
    
    Returns a series of x and t."""
    
    # Defining local variables for conciseness
    t0 = params['t0']
    tf = params['tf']
    dt = params['dt']
    x0 = params['x0']
    f = lambda x, t : params['f'](x, t, params)
    exact = lambda t : params['exact'](t, params)
    
    # Time series to return
    ts = []
    xs = []
    
    # Solution loop
    t = t0
    x = x0
    ts += [t]
    xs += [x]
    # print(f'time: {t:.2f}\texact: {exact(t):8.4f}\tnumerical:{x:8.4f}')
    while t < tf:
        if np.abs(tf - t) < np.abs(dt):
            dt = tf - t
        x = euler_step(f, x, t, dt)
        t += dt
        ts += [t]
        xs += [x]
        # print(f'time: {t:.2f}\texact: {exact(t):8.4f}\tnumerical:{x:8.4f}')
    return ts, xs



def euler_step(f, xn: float, tn: float, dt: float):
    """Apply the Forward Euler method for one time step."""
    
    return xn + dt * f(xn, tn)



if __name__ == '__main__':
    main()