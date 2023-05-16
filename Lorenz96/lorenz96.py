import numpy as np

def lorenz96(initial_state, nsteps):
    """
    Perform iterations of the Lorenz 96 update.

    Parameters
    ----------
    initial_state : array_like or list
        Initial state of lattice in an array of floats.
    nsteps : int
        Number of steps of Lorenz 96 to perform.

    Returns
    -------

    numpy.ndarray
         Final state of lattice in array of floats

    >>> x = lorenz96([8.0, 8.0, 8.0], 1)
    >>> print(x)
    array([8.0, 8.0, 8.0])

    >>> lorenz96([False, False, True, False, False], 3)
    array([True, False, True, True, True])
    """

    #print(updated_state)
    new_state = np.array(initial_state, np.float64)
    
    for _ in range(nsteps):
        old_state = new_state.copy()
        for index in range(len(initial_state)):
            if index < len(initial_state) - 1:
                new_state[index] = (100 * old_state[index] + (old_state[index - 2] - old_state[index + 1]) * old_state[index - 1] + 8) / 101
            else:
                new_state[index] = (100 * old_state[index] + (old_state[index - 2] - old_state[0]) * old_state[index - 1] + 8) / 101
    
    return new_state