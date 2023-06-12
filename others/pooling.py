from multiprocessing import Pool

with Pool(processes = 6) as mp_pool:
    for i in range(100):
        print(i)