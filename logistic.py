import numpy as np

def logistic(x):   
    
    # Dr Jesús Rubio
    # University of Exeter
    # J.Rubio-Jimenez@exeter.ac.uk
    #
    # Created: May 2022
    # Last modified: --
    #
    # Returns the logistic function f(x) = 1/(1+exp(-x)) evaluated at x
    
    y=1./(1+np.exp(-x))

    return y
