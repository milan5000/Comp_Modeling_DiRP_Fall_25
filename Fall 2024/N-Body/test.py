import numpy as np
import my_integrators as mi

def main():
    print('A very old differential equation from Mr. Newton himself')
    f = lambda t, y: 1 - 3 * t + y + t ** 2 + t * y
    
    methods = [
        'explicit_euler',
        'explicit_rk2',
        'explicit_rk4'
    ]

if __name__ == '__main__':
	main()