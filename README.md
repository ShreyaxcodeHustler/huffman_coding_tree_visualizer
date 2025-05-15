# huffman_coding_tree_visualizer


A graphical user interface application that implements Huffman coding for text compression and decompression. This project demonstrates the implementation of the Huffman coding algorithm with a user-friendly interface.

## Features

- **Text Encoding**: Convert input text into Huffman codes
- **Text Decoding**: Decode Huffman codes back to original text
- **Code Visualization**: View the generated Huffman codes for each character
- **Tree Visualization**: Display the Huffman tree structure
- **User-Friendly Interface**: Simple and intuitive GUI design

## Requirements

- Python 3.x
- tkinter (usually comes with Python installation)
- collections (standard library)
- heapq (standard library)

## Installation

1. Clone this repository or download the source code
2. Ensure you have Python installed on your system
3. No additional package installation is required as all dependencies are part of the Python standard library

## Usage

1. Run the program:
   ```bash
   python "huffman's coding.py"
   ```

2. The GUI will open with the following options:
   - Enter text in the input area
   - Click "Encode" to compress the text using Huffman coding
   - Click "Decode" to decompress the encoded text
   - Click "Show Codes" to view the Huffman codes for each character
   - Click "Show Tree" to visualize the Huffman tree structure

## How It Works

1. **Encoding Process**:
   - Counts frequency of each character in the input text
   - Builds a Huffman tree based on character frequencies
   - Generates binary codes for each character
   - Encodes the input text using the generated codes

2. **Decoding Process**:
   - Uses the Huffman tree to decode the binary sequence
   - Reconstructs the original text from the encoded data

## Implementation Details

The project is implemented using:
- `tkinter` for the graphical user interface
- `collections.Counter` for frequency counting
- `heapq` for priority queue implementation
- Custom `Node` class for Huffman tree construction

## License

This project is open source and available for educational purposes.

## Author

Created as part of the ADA mini project. 
