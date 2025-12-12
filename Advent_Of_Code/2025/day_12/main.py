import sys
import os


def normalize_shape(coords):
    if not coords: return tuple()
    min_r = min(r for r, c in coords)
    min_c = min(c for r, c in coords)
    return tuple(sorted((r - min_r, c - min_c) for r, c in coords))

def rotate_shape(coords):
    return [(c, -r) for r, c in coords]

def flip_shape(coords):
    return [(r, -c) for r, c in coords]

def generate_orientations(grid_lines):
    initial_coords = []
    for r, row in enumerate(grid_lines):
        for c, char in enumerate(row):
            if char == '#':
                initial_coords.append((r, c))
    
    unique_shapes = set()
    current = initial_coords
    for _ in range(4):
        unique_shapes.add(normalize_shape(current))
        unique_shapes.add(normalize_shape(flip_shape(current)))
        current = rotate_shape(current)
    return list(unique_shapes)

def parse_input(raw_input):
    sections = raw_input.strip().split('\n\n')
    shape_blocks = sections[:-1]
    query_block = sections[-1]
    
    shapes = {}
    for block in shape_blocks:
        lines = block.strip().split('\n')
        idx = int(lines[0].replace(':', ''))
        shapes[idx] = generate_orientations(lines[1:])
        
    queries = []
    for line in query_block.strip().split('\n'):
        if not line: continue
        dims, counts = line.split(':')
        W, L = map(int, dims.strip().split('x'))
        
        pieces_to_fit = []
        for s_idx, count in enumerate(map(int, counts.strip().split())):
            for _ in range(count):
                pieces_to_fit.append(s_idx)
        
        pieces_to_fit.sort(key=lambda x: len(shapes[x][0]), reverse=True)
        
        queries.append({'W': W, 'L': L, 'pieces': pieces_to_fit})
        
    return shapes, queries


class BitmaskSolver:
    def __init__(self, W, L, shapes_meta, pieces):
        self.W = W
        self.L = L
        self.pieces = pieces
        
        self.move_masks = {}
        
        unique_ids = set(pieces)
        for pid in unique_ids:
            valid_moves = []
            orientations = shapes_meta[pid]
            
            seen_masks = set()
            
            for shape in orientations:
                shape_h = max(r for r,c in shape) + 1
                shape_w = max(c for r,c in shape) + 1
                
                # Slide over the board
                for r in range(self.L - shape_h + 1):
                    for c in range(self.W - shape_w + 1):
                        
                        mask = 0
                        for (br, bc) in shape:
                            pos = (r + br) * self.W + (c + bc)
                            mask |= (1 << pos)
                        
                        if mask not in seen_masks:
                            seen_masks.add(mask)
                            linear_index = r * self.W + c
                            valid_moves.append((mask, linear_index))
            
            valid_moves.sort(key=lambda x: x[1])
            self.move_masks[pid] = valid_moves

    def solve(self):
        return self._dfs(0, 0, -1)

    def _dfs(self, piece_idx, current_board, last_pos_index):
        if piece_idx == len(self.pieces):
            return True

        p_id = self.pieces[piece_idx]
        
        start_search_index = -1
        if piece_idx > 0 and self.pieces[piece_idx] == self.pieces[piece_idx-1]:
            start_search_index = last_pos_index

        possible_moves = self.move_masks[p_id]

        for mask, linear_pos in possible_moves:
            if linear_pos < start_search_index:
                continue

            if (current_board & mask) == 0:
                if self._dfs(piece_idx + 1, current_board | mask, linear_pos):
                    return True
                    
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python day12.py <input_file>")
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print("File not found.")
        sys.exit(1)
        
    with open(filename, 'r') as f:
        raw = f.read()

    shapes, queries = parse_input(raw)
    
    print(f"Processing {len(queries)} regions...")
    success_count = 0
    
    for i, q in enumerate(queries):
        W, L = q['W'], q['L']
        pieces = q['pieces']
        
        total_area = W * L
        pieces_area = sum(len(shapes[p][0]) for p in pieces)
        
        if pieces_area > total_area:
            print(f"Region {i+1}: Failed (Area Overflow)")
            continue
            
        solver = BitmaskSolver(W, L, shapes, pieces)
        if solver.solve():
            print(f"Region {i+1}: Success")
            success_count += 1
        else:
            print(f"Region {i+1}: Failed")
            
    print(f"\nAnswer: {success_count}")

if __name__ == "__main__":
    main()
