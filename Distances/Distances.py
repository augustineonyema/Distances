import numpy as np
import pandas as pd

def sq(a):
    """
    This code calculates the Conditional activity (Time correlated transition) of a degree of freedom. In this case, the sidechain dihedral (chi) angles per frame\
    for selected residues except ALA, GLY. The code seek to find the kinetic correlation of amino acids side chain in the 3-dimensional native state of a protein.\
    The module is build using other MDAnalysis function as a foundation.
    
    input: The residue id and names of amino acids of interest.\
        Number of states adopted by amino acid side chain.\
        
    output: csv file containing values for each residue for each frame
    """
    g = a**2
    return g

print(sq(4))
