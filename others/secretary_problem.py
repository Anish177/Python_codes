from math import e
from numpy.random import randint
from multiprocessing import Pool

'''
tries to solve secretary problem by choosing the best from the second half of the queue
'''


def queue() -> int:
    '''
    returns a random number between 1 and 100
    '''
    yield randint(1, 100)


def secretary(number: int) -> bool:
    # '''
    # takes number of objects coming in
    # returns the best one found after neglecting the first half,
    # using that data to find the best in rest
    # '''
    '''
    now returns a boolean True if a best was found in second half
    '''
    e_1 = int(number // e)
    rejected = [next(queue()) for _ in range(e_1)]
    max_rejected = max(rejected)

    for _ in range(e_1 + 1, number + 1):
        current = next(queue())
        if current > max_rejected:
            return True
        rejected.append(current)

    return False


tests = [secretary(100) for _ in range(100)]
print(tests.count(True)/len(tests))