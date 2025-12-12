import sys

def getRanges(file: str) -> list[list[str]]:
    with open(file) as f:
        return [s.strip().split('-') for s in f.read().split(',')]

def solve():
    if len(sys.argv) != 2:
        print("Usage python3 ./main.py data.txt")
        sys.exit(-1)

    ranges = getRanges(sys.argv[1])
    global_invalid_ids = set()

    for start_s, end_s in ranges:
        start_val = int(start_s)
        end_val = int(end_s)
        for current_len in range(len(start_s), len(end_s) + 1):
            for pat_len in range(1, current_len // 2 + 1):
                if current_len % pat_len == 0:
                    pat_start = 10**(pat_len - 1)
                    pat_end = 10**pat_len
                    for p in range(pat_start, pat_end):
                        pattern_str = str(p)
                        candidate_str = pattern_str * (current_len // pat_len)
                        candidate_val = int(candidate_str)
                        if start_val <= candidate_val <= end_val:
                            global_invalid_ids.add(candidate_val)

    print(sum(global_invalid_ids))

if __name__ == "__main__":
    solve()
