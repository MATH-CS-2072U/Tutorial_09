import numpy as np
import matplotlib.pyplot as plt
from simpson import simpson

def simpson( ... ):                                     # Composite Simpson integration for int(f(x),x=a..b) on n intervals.
    xs = np.linspace( ... )                             # Array xs holds the interval boundaries as well as the mid points.
    I = 0.0                                             # Initialize I.
    h = ...                                             # Pre-factor in Simpson's method
    for k in range(0,2*n-1,2):                          # Loop over intervals.
        I = I + ...                                     # Add approximate integral over interval k/2.
    I = h * I                                           # Factor in pre-factor.
    return I

def f(x):                              # Test function
    return np.exp(np.sin(x)+1)

ntest = 10                             # Compare ntest numbers of intervals
l = 0                                  # Left and right boundary of the integral
r = 2
a = np.zeros((ntest,2))                # Pre-allocate array for approximate results

for k in range(0,ntest):               # Loop over number of intervals
    n = ...                            # Set number of intervals
    I = simpson( ... )                 # Approximate the integral using composite Simpson
    a[k,0] = n                         # Store result
    a[k,1] = I
print(a)                               # Display results and plot consecutive differences
plt.loglog(a[1:ntest+1,0],abs(np.diff(a[:,1])),'-*',a[1:ntest+1,0],a[1:ntest+1,0]**(-4),'-r')
plt.xlabel('number of intervals')
plt.ylabel('Difference between consecutive approximations')
plt.title('Red line indicates O(1/n^4)')
plt.show()
# Note, that on every interval the error is of order O(h**(-5))=O(1/n**5) and we have n intervals, so the total error decays as O(1/n**4).
