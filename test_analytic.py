import unittest

from analytic import Wall


class Analytic(unittest.TestCase):

    def test_wall(self):
        w = Wall(conductivity=0.6,
                 density=1000,
                 heat_capacity=4200,
                 width=0.1,
                 initial_condition=300,
                 boundary_condition=[1, 330]  # [2, 1000], [3, 330, 10]
                 )
        temperature = w(x=1, y=2, z=3, t=1)
        print(temperature)


if __name__ == '__main__':
    unittest.main()
