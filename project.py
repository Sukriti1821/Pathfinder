import tkinter as tk
from tkinter import simpledialog, messagebox
import heapq

class DijkstraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dijkstra Path Finder")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.nodes = {}
        self.edges = {}
        self.node_count = 0

        self.start_node = None

        # Bind mouse click
        self.canvas.bind("<Button-1>", self.add_node)

        # Buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        tk.Button(self.button_frame, text="Connect Nodes", command=self.connect_nodes).pack(side=tk.LEFT)
        tk.Button(self.button_frame, text="Run Dijkstra", command=self.run_dijkstra).pack(side=tk.LEFT)
    
    def add_node(self, event):
        node_name = f"N{self.node_count}"
        self.nodes[node_name] = (event.x, event.y)
        self.edges[node_name] = []

        self.canvas.create_oval(event.x-15, event.y-15, event.x+15, event.y+15, fill="lightblue")
        self.canvas.create_text(event.x, event.y, text=node_name)
        
        self.node_count += 1

    def connect_nodes(self):
        node1 = simpledialog.askstring("Input", "Enter first node (e.g., N0):")
        node2 = simpledialog.askstring("Input", "Enter second node (e.g., N1):")
        if node1 not in self.nodes or node2 not in self.nodes:
            messagebox.showerror("Error", "Invalid node names!")
            return
        try:
            weight = int(simpledialog.askstring("Input", "Enter weight (distance) between nodes:"))
        except:
            messagebox.showerror("Error", "Weight must be an integer!")
            return

        self.edges[node1].append((node2, weight))
        self.edges[node2].append((node1, weight))

        x1, y1 = self.nodes[node1]
        x2, y2 = self.nodes[node2]
        self.canvas.create_line(x1, y1, x2, y2)
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        self.canvas.create_text(mx, my, text=str(weight), fill="red")

    def run_dijkstra(self):
        self.start_node = simpledialog.askstring("Input", "Enter start node:")
        if self.start_node not in self.nodes:
            messagebox.showerror("Error", "Invalid start node!")
            return

        distances = self.dijkstra(self.start_node)

        result = ""
        for node, distance in distances.items():
            result += f"Distance from {self.start_node} to {node}: {distance}\n"

        messagebox.showinfo("Result", result)

    def dijkstra(self, start):
        queue = [(0, start)]
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.edges[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances

if __name__ == "__main__":
    root = tk.Tk()
    app = DijkstraGUI(root)
    root.mainloop()
