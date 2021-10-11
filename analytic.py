class Wall:
    def __init__(self, conductivity, density, heat_capacity, width,
                 initial_condition, boundary_condition, **kwargs):
        """Wall
        Args:
            boundary_condition(list of float):
            dirichlet - [1, temperature],
            neumann - [2, heat flux],
            robin - [3, temperature, heat transfer (film) coefficient]
        """
        self.c = conductivity
        self.d = density
        self.hc = heat_capacity
        self.w = width
        self.ic = initial_condition
        self.bc = boundary_condition

    def __call__(self, x, y, z, t, **kwargs):
        return 42
