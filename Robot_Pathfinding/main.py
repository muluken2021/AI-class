import tkinter as tk
import time

# Ensure your local files (bfs.py, dfs.py, astar.py) are in the same folder
from bfs import bfs
from dfs import dfs
from astar import astar
from ucs import ucs
from dls import dls
from iddfs import iddfs
from bs import bs
from gs import gs

# --- Configuration & Styling ---
GRID = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

ROWS, COLS = 5, 5
CELL_SIZE = 70  # Slightly larger for better visibility
COLORS = {
    "bg": "#f0f2f5",      # Light modern gray
    "obstacle": "#34495e", # Dark slate
    "path": "#3498db",     # Bright blue
    "start": "#2ecc71",    # Emerald green
    "goal": "#e74c3c",     # Alizarin red
    "grid": "#bdc3c7",     # Silver
    "robot": "#f1c40f"     # Robot yellow
}

START = (0, 0)
GOAL = (4, 3)

class PathfindingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Robot Pathfinding Pro")
        self.root.configure(bg=COLORS["bg"])

        # Canvas Setup
        self.canvas = tk.Canvas(
            root, 
            width=COLS * CELL_SIZE, 
            height=ROWS * CELL_SIZE, 
            bg="white", 
            highlightthickness=0
        )
        self.canvas.pack(pady=20, padx=20)

        # UI Controls Frame
        self.btn_frame = tk.Frame(root, bg=COLORS["bg"])
        self.btn_frame.pack(pady=10)

        self.create_buttons()
        self.draw_grid()

    def create_buttons(self):
        btn_style = {
            "font": ("Arial", 10, "bold"),
            "fg": "white",
            "padx": 15,
            "pady": 5,
            "bd": 0,
            "cursor": "hand2"
        }

        tk.Button(self.btn_frame, text="BFS", bg="#9b59b6", command=self.run_bfs, **btn_style).pack(side=tk.LEFT, padx=5)
        tk.Button(self.btn_frame, text="DFS", bg="#8e44ad", command=self.run_dfs, **btn_style).pack(side=tk.LEFT, padx=5)
        tk.Button(self.btn_frame, text="A*", bg="#2980b9", command=self.run_astar, **btn_style).pack(side=tk.LEFT, padx=5)
        tk.Button(self.btn_frame, text="RESTART", bg="#e67e22", command=self.draw_grid, **btn_style).pack(side=tk.LEFT, padx=20)
        tk.Button(self.btn_frame, text="UCS", bg="#16a085", command=self.run_ucs, **btn_style).pack(side=tk.LEFT, padx=5)

        tk.Button(self.btn_frame, text="DLS", bg="#27ae60", command=self.run_dls, **btn_style).pack(side=tk.LEFT, padx=5)
        tk.Button(self.btn_frame, text="IDDFS", bg="#f39c12", command=self.run_iddfs, **btn_style).pack(side=tk.LEFT, padx=5)
        tk.Button(self.btn_frame, text="BIDIR", bg="#d35400", command=self.run_bidirectional, **btn_style).pack(side=tk.LEFT, padx=5)
        tk.Button(self.btn_frame, text="GREEDY", bg="#2c3e50", command=self.run_greedy, **btn_style).pack(side=tk.LEFT, padx=5)

    def draw_grid(self):
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                x1, y1 = c * CELL_SIZE, r * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                
                if GRID[r][c] == 1:
                    # Modern Obstacle: Crate with an 'X'
                    self.canvas.create_rectangle(x1+5, y1+5, x2-5, y2-5, fill="#34495e", outline="#2c3e50")
                    self.canvas.create_line(x1+10, y1+10, x2-10, y2-10, fill="#2c3e50", width=2)
                    self.canvas.create_line(x1+10, y2-10, x2-10, y1+10, fill="#2c3e50", width=2)
                elif (r, c) == START:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=COLORS["start"], outline=COLORS["grid"])
                    self.canvas.create_text(x1+35, y1+35, text="START", font=("Arial", 8, "bold"), fill="white")
                elif (r, c) == GOAL:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=COLORS["goal"], outline=COLORS["grid"])
                    self.canvas.create_text(x1+35, y1+35, text="GOAL", font=("Arial", 8, "bold"), fill="white")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline=COLORS["grid"])
                    
    def animate_robot(self, path):
        if not path:
            return

        # --- Create Blocky Robot ---
        # 1. Antennas
        ant_l = self.canvas.create_line(0,0,0,0, fill="#7f8c8d", width=2, tags="robot")
        ant_r = self.canvas.create_line(0,0,0,0, fill="#7f8c8d", width=2, tags="robot")
        # 2. Main Head
        head = self.canvas.create_rectangle(0,0,0,0, fill="#95a5a6", outline="#7f8c8d", width=2, tags="robot")
        # 3. Visor
        visor = self.canvas.create_rectangle(0,0,0,0, fill="#2c3e50", outline="", tags="robot")
        # 4. Glowing Eyes
        eye_l = self.canvas.create_oval(0,0,0,0, fill="#00ffff", outline="", tags="robot")
        eye_r = self.canvas.create_oval(0,0,0,0, fill="#00ffff", outline="", tags="robot")

        for (r, c) in path:
            # Draw Path trail behind
            if (r, c) != START and (r, c) != GOAL:
                self.canvas.create_oval(c*CELL_SIZE+25, r*CELL_SIZE+25, c*CELL_SIZE+45, r*CELL_SIZE+45,
                                        fill=COLORS["path"], outline="", stipple="gray50")

            # Calculate coordinates for the new cell
            x, y = c * CELL_SIZE, r * CELL_SIZE
            pad = 15
            
            # Move all Robot parts
            self.canvas.coords(ant_l, x+30, y+10, x+25, y+5)
            self.canvas.coords(ant_r, x+40, y+10, x+45, y+5)
            self.canvas.coords(head, x+pad, y+pad, x+CELL_SIZE-pad, y+CELL_SIZE-pad)
            self.canvas.coords(visor, x+pad+5, y+pad+8, x+CELL_SIZE-pad-5, y+pad+18)
            self.canvas.coords(eye_l, x+30, y+pad+11, x+34, y+pad+15)
            self.canvas.coords(eye_r, x+38, y+pad+11, x+42, y+pad+15)
            
            self.root.update()
            time.sleep(0.15)

    def run_bfs(self):
        self.draw_grid()
        path = bfs(GRID, START, GOAL)
        self.animate_robot(path)

    def run_dfs(self):
        self.draw_grid()
        path = dfs(GRID, START, GOAL)
        self.animate_robot(path)

    def run_astar(self):
        self.draw_grid()
        # Adjusted for the common (visited, path) return of A*
        result = astar(GRID, START, GOAL)
        path = result[1] if isinstance(result, tuple) else result
        self.animate_robot(path)
        
    def run_ucs(self):
        self.draw_grid()
        path = ucs(GRID, START, GOAL)
        self.animate_robot(path)
        
    def run_dls(self):
        self.draw_grid()
        path = dls(GRID, START, GOAL, 10)
        self.animate_robot(path)
        
    def run_iddfs(self):
        self.draw_grid()
        path = iddfs(GRID, START, GOAL)
        self.animate_robot(path)
        
    def run_bidirectional(self):
        self.draw_grid()
        path = bs(GRID, START, GOAL)
        self.animate_robot(path)
        
    def run_greedy(self):
        self.draw_grid()
        path = gs(GRID, START, GOAL)
        self.animate_robot(path)

if __name__ == "__main__":
    root = tk.Tk()
    app = PathfindingVisualizer(root)
    root.mainloop()