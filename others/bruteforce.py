import hashlib
import itertools
from multiprocessing import Pool


def brute_force(hash_to_crack, charset, hash_algorithm):
    # Define the hash function to use
    if hash_algorithm == "sha1":
        hash_function = hashlib.sha1
    elif hash_algorithm == "md5":
        hash_function = hashlib.md5
    else:
        raise ValueError("Invalid hash algorithm")
    
    # Generate all possible combinations of characters
    with Pool(processes = 2) as mp_pool:
        for length in range(1, len(charset)):
            for combination in itertools.product(charset, repeat=length):
                candidate = "".join(combination)
                candidate_hash = hash_function(candidate.encode()).hexdigest()
                if candidate_hash == hash_to_crack:
                    return candidate
    return None

hash_to_crack = '9cf95dacd226dcf43da376cdb6cbba7035218921' # input("Enter the hash to crack: ")

# Define the charset to use
charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

hash_algorithm = 'sha1' # input("Enter the hash algorithm to use (sha256 or md5): ")

result = brute_force(hash_to_crack, charset, hash_algorithm)

if result is None:
    print("No match found.")
else:
    print("Match found:", result)
