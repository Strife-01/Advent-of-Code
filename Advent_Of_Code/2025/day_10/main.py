import sys
import numpy as np
from scipy.optimize import linprog, milp, LinearConstraint, Bounds

def main():
    data = parseData()
    s = 0
    failed = []
    for idx, (_, buttons, output) in enumerate(data):
        result = solve_machine(output, buttons, idx)
        if result is not None:
            s += result
        else:
            failed.append(idx)
    
    if failed:
        print(f"Failed machines: {len(failed)} out of {len(data)}")
        print(f"Indices: {failed[:10]}{'...' if len(failed) > 10 else ''}")
    print(f"Total: {s}")

def parseData():
    ret = []
    with open(sys.argv[1]) as f:
        for l in f:
            line_comp = l.strip().split()
            target_str = line_comp[-1].lstrip('{').rstrip('}')
            target = [int(x) for x in target_str.split(',')]
            
            buttons = []
            for i in range(1, len(line_comp) - 1):
                button_str = line_comp[i].lstrip('(').rstrip(')')
                button_indices = set([int(x) for x in button_str.split(',')])
                buttons.append(button_indices)
            
            ret.append((line_comp[0], buttons, target))
    return ret

def solve_machine(target, buttons, idx=None):
    """
    Use integer linear programming to find minimum button presses.
    Minimize sum(x) subject to A*x = b, x >= 0, x integer.
    """
    num_eq = len(target)
    num_vars = len(buttons)
    
    A = np.zeros((num_eq, num_vars), dtype=np.float64)
    for col, indices in enumerate(buttons):
        for row in indices:
            if row < num_eq:
                A[row, col] = 1.0
    
    b = np.array(target, dtype=np.float64)
    
    c = np.ones(num_vars)
    
    constraints = LinearConstraint(A, b, b)
    
    bounds = Bounds(0, np.inf)
    
    integrality = np.ones(num_vars)
    
    try:
        result = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)
        
        if result.success:
            x = np.round(result.x).astype(np.int64)
            
            check = np.zeros(num_eq, dtype=np.int64)
            for col in range(num_vars):
                for row in buttons[col]:
                    if row < num_eq:
                        check[row] += x[col]
            
            if np.array_equal(check, target):
                return int(np.sum(x))
        
        if idx is not None and idx < 10:
            print(f"Machine {idx}: MILP failed, trying LP relaxation")
        
        return solve_with_lp(A, b, buttons, target, idx)
        
    except Exception as e:
        if idx is not None and idx < 10:
            print(f"Machine {idx}: MILP error: {e}")
        return solve_with_lp(A, b, buttons, target, idx)

def solve_with_lp(A, b, buttons, target, idx=None):
    """Fallback: solve LP relaxation and try to find integer solution."""
    num_eq = len(target)
    num_vars = len(buttons)
    
    c = np.ones(num_vars)
    
    result = linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method='highs')
    
    if result.success:
        x = result.x
        
        for strategy in ['round', 'floor', 'ceil']:
            if strategy == 'round':
                x_test = np.round(x)
            elif strategy == 'floor':
                x_test = np.floor(x)
            else:
                x_test = np.ceil(x)
            
            x_test = np.maximum(x_test, 0).astype(np.int64)
            
            check = np.zeros(num_eq, dtype=np.int64)
            for col in range(num_vars):
                for row in buttons[col]:
                    if row < num_eq:
                        check[row] += x_test[col]
            
            if np.array_equal(check, target):
                return int(np.sum(x_test))
    
    if idx is not None and idx < 10:
        print(f"Machine {idx}: All strategies failed")
    
    return None

if __name__ == "__main__":
    main()
