import tkinter as tk
from tkinter import scrolledtext, messagebox
from collections import Counter
import heapq

# Node for Huffman Tree
class Node:
   def __init__(self, char=None, freq=0):
       self.char = char
       self.freq = freq
       self.left = None
       self.right = None

   def __lt__(self, other):
       return self.freq < other.freq

# Build Huffman Tree
def build_tree(text):
   freq_map = Counter(text)
   heap = [Node(char, freq) for char, freq in freq_map.items()]
   heapq.heapify(heap)

   while len(heap) > 1:
       left = heapq.heappop(heap)
       right = heapq.heappop(heap)
       merged = Node(None, left.freq + right.freq)
       merged.left = left
       merged.right = right
       heapq.heappush(heap, merged)

   return heap[0]

# Generate Huffman Codes
def generate_codes(node, current_code="", codes={}):
   if node is None:
       return

   if node.char is not None:
       codes[node.char] = current_code

   generate_codes(node.left, current_code + "0", codes)
   generate_codes(node.right, current_code + "1", codes)
   return codes

# Print tree as string
def print_tree(node, indent=""):
   if node is None:
       return ""
   result = ""
   if node.char:
       result += indent + f"'{node.char}' ({node.freq})\n"
   else:
       result += indent + f"[{node.freq}]\n"
   result += print_tree(node.left, indent + "  ├─")
   result += print_tree(node.right, indent + "  └─")
   return result

# Encode
def encode_text():
   global huffman_root, huffman_codes, encoded_result
   text = input_text.get("1.0", tk.END).strip()
   if not text:
       messagebox.showwarning("Empty Input", "Please enter some text to encode.")
       return

   huffman_root = build_tree(text)
   huffman_codes = generate_codes(huffman_root, "", {})
   encoded_result = ''.join(huffman_codes[char] for char in text)

   output_text.delete("1.0", tk.END)
   output_text.insert(tk.END, "✅ Encoded Text:\n" + encoded_result)

# Decode
def decode_text():
   if not encoded_result:
       messagebox.showwarning("No Encoded Data", "Please encode some text first.")
       return

   reverse_codes = {v: k for k, v in huffman_codes.items()}
   current_code = ""
   decoded = ""

   for bit in encoded_result:
       current_code += bit
       if current_code in reverse_codes:
           decoded += reverse_codes[current_code]
           current_code = ""

   output_text.delete("1.0", tk.END)
   output_text.insert(tk.END, "🪄 Decoded Text:\n" + decoded)

# Show codes
def show_codes():
   if not huffman_codes:
       messagebox.showwarning("No Data", "Please encode some text first.")
       return
   output_text.delete("1.0", tk.END)
   output_text.insert(tk.END, "🔢 Huffman Codes:\n")
   for char, code in huffman_codes.items():
       output_text.insert(tk.END, f"'{char}': {code}\n")

# Show tree
def show_tree():
   if not huffman_root:
       messagebox.showwarning("No Tree", "Please encode some text first.")
       return
   tree_str = print_tree(huffman_root)
   output_text.delete("1.0", tk.END)
   output_text.insert(tk.END, "🌳 Huffman Tree:\n" + tree_str)

# GUI Setup
root = tk.Tk()
root.title("🧠 Huffman Coding GUI")
root.geometry("800x600")

huffman_root = None
huffman_codes = {}
encoded_result = ""

tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack(pady=5)
input_text = scrolledtext.ScrolledText(root, height=4, font=("Consolas", 12))
input_text.pack(fill="x", padx=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Encode", width=12, bg="#d4edda", command=encode_text).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Decode", width=12, bg="#ffeeba", command=decode_text).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Show Codes", width=12, bg="#cce5ff", command=show_codes).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Show Tree", width=12, bg="#f8d7da", command=show_tree).grid(row=0, column=3, padx=5)

tk.Label(root, text="Output:", font=("Arial", 12)).pack(pady=5)
output_text = scrolledtext.ScrolledText(root, height=20, font=("Consolas", 12))
output_text.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()

