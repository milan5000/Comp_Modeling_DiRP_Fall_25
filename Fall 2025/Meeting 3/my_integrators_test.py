import numpy as np
import my_integrators
import my_integrators_solution
import matplotlib.pyplot as plt

def lv_eqs(t, x):
    # assume x is np array with x[0] = N, x[1] = P
    # return x[0] = dN/dt, x[1] = dP/dt
    A = 5
    B = 0.05
    C = 0.005
    D = 5
    return np.array([A*x[0] - B*x[0]*x[1], C*x[0]*x[1] - D*x[1]])

def main():
    method = "explicit_rk4"
    tspan = (0.0, 10.0)
    init_prey_pred = np.array([100.0, 100.0])
    dt = 0.1

    time_vec, state_vec = my_integrators.ode_integrator(method, lv_eqs, tspan, init_prey_pred, dt)
    time_np = np.array(time_vec)
    prey_np = np.array([state[0] for state in state_vec])
    pred_np = np.array([state[1] for state in state_vec])

    plt.figure(figsize=(8, 6))

    plt.plot(time_np, prey_np, label='Prey Population', color='blue', linestyle='-')
    plt.plot(time_np, pred_np, label='Predator Population', color='red', linestyle='--')

    plt.xlabel('Time')
    plt.ylabel('Population')
    plt.title('Lotka-Volterra Equations')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
