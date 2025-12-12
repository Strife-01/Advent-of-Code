import sys
from itertools import combinations

def parse_data():
    ret = []
    with open(sys.argv[1]) as f:
        for line in f:
            parts = line.strip().split()
            
            target = parts[0].strip('[]')
            
            buttons = []
            for i in range(1, len(parts) - 1):
                button_str = parts[i].strip('()')
                button_indices = set(int(x) for x in button_str.split(','))
                buttons.append(button_indices)
            
            ret.append((target, buttons))
    return ret

def gauss_eliminate_gf2(matrix, target):
    """
    Solve Ax = b in GF(2) using Gaussian elimination.
    Returns (solution, free_variables) where free_variables are column indices.
    """
    n_lights = len(matrix)
    n_buttons = len(matrix[0]) if n_lights > 0 else 0
    
    aug = [row[:] + [target[i]] for i, row in enumerate(matrix)]
    
    pivot_cols = []
    current_row = 0
    
    for col in range(n_buttons):
        pivot_row = None
        for row in range(current_row, n_lights):
            if aug[row][col] == 1:
                pivot_row = row
                break
        
        if pivot_row is None:
            continue
        
        aug[current_row], aug[pivot_row] = aug[pivot_row], aug[current_row]
        pivot_cols.append(col)
        
        for row in range(n_lights):
            if row != current_row and aug[row][col] == 1:
                for c in range(n_buttons + 1):
                    aug[row][c] ^= aug[current_row][c]
        
        current_row += 1
    
    for row in range(current_row, n_lights):
        if aug[row][-1] == 1:
            return None, None
    
    solution = [0] * n_buttons
    for i, col in enumerate(pivot_cols):
        solution[col] = aug[i][-1]
    
    free_vars = [col for col in range(n_buttons) if col not in pivot_cols]
    
    return solution, free_vars, aug, pivot_cols

def solve_machine(target, buttons):
    """
    Solve for minimum button presses for one machine.
    """
    n_lights = len(target)
    n_buttons = len(buttons)
    
    matrix = []
    for light in range(n_lights):
        row = []
        for button in buttons:
            row.append(1 if light in button else 0)
        matrix.append(row)
    
    target_vec = [1 if c == '#' else 0 for c in target]
    
    result = gauss_eliminate_gf2(matrix, target_vec)
    if result[0] is None:
        return float('inf')
    
    particular_solution, free_vars, aug, pivot_cols = result
    
    if not free_vars:
        return sum(particular_solution)
    
    min_presses = sum(particular_solution)
    
    for num_free in range(1, len(free_vars) + 1):
        for free_combo in combinations(free_vars, num_free):
            test_solution = particular_solution[:]
            for fv in free_combo:
                test_solution[fv] = 1
            
            for i, pivot_col in enumerate(pivot_cols):
                test_solution[pivot_col] = aug[i][-1]
                for col in range(n_buttons):
                    if col != pivot_col:
                        test_solution[pivot_col] ^= (aug[i][col] & test_solution[col])
            
            presses = sum(test_solution)
            min_presses = min(min_presses, presses)
    
    return min_presses

def main():
    data = parse_data()
    total_presses = 0
    
    for target, buttons in data:
        presses = solve_machine(target, buttons)
        print(f"Target: {target}, Buttons: {len(buttons)}, Min presses: {presses}")
        total_presses += presses
    
    print(f"\nTotal minimum button presses: {total_presses}")

if __name__ == "__main__":
    main()
