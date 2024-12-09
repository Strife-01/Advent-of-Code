import hashlib
import sys

def return_md5_hex_hash(string, nr_zeros) -> str:
    return hashlib.md5(string.encode()).hexdigest()

def iterate_numbers_as_prefixes(input, nr_zeros) -> str:
    i = 0
    while True:
        if return_md5_hex_hash(f'{input}{i}', nr_zeros).startswith('0' * nr_zeros):
            return f'{i}'
        i += 1

print(iterate_numbers_as_prefixes(sys.argv[1], int(sys.argv[2])))
