import numpy as np
import my_integrators as mi

def main():
    print('A very old differential equation')
    f = lambda t, y: 1 - 3 * t + y + t ** 2 + t * y

if __name__ == '__main__':
	main()