# Physics 91SI
# Spring 2015
# Lab 8

import numpy as np

class Particle:
    """Stores information about a particle with mass, position, and velocity."""
    
    def __init__(self, Position, M):
        """Create a particle with position (numpy array of len 2) and mass."""
        self.pos = Position   # Sets (x,y) position
        self.m = M  # Sets mass
        # Initial velocity and acceleration set to be zero
        self.vel = np.zeros((2,))
        self.acc = np.zeros((2,))

        
class Molecule: 
    """Stores information about a diatomic molecule with two particles, a spring constant, and equilibrium length."""
    
    def __init__(self, pos1, pos2, m1, m2, spring_const, equil_length):
    """Create Particles p1 and p2 inside boundaries and return a molecule
    connecting them"""
    self.p1 = Particle(pos1, m1)
    self.p2 = Particle(pos2, m2)
    self.k = spring_const
    self.L0 = equil_length
    
    def get_disp1(self):
        return tuple(np.subtract(self.p2.pos, self.p1.pos))

    def get_force(self):
        return self.k * get_disp1(self)
