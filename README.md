## Project: Rubik's Cube Color Detection and Visualization

### Overview

This project is designed to detect and visualize the colors on the faces of a Rubik's Cube using a webcam. The program captures images of each face of the Rubik's Cube, processes the colors, and displays them in a 2D representation. It utilizes OpenCV for image processing and color detection and uses the Kociemba algorithm (imported but not used in the main code) to potentially solve the Rubik's Cube based on the detected colors.

### Requirements

- **Python 3.x**
- **OpenCV 4.x** (`cv2`)
- **NumPy** (`numpy`)
- **Kociemba Python package** (`kociemba`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/arundeegutla/Rubixolver.git
   cd Rubixolver
   ```

2. **Install the required packages:**
   ```bash
   pip install opencv-python numpy kociemba
   ```

### Code Explanation

1. **Side Class:**
   - The `Side` class represents one face of the Rubik's Cube. Each face is a 2D array (4x4) of colors initialized to `'NULL'`.

2. **get_color Function:**
   - Determines the dominant color of a cubelet based on the average red, green, and blue values from the captured image.

3. **put_sides Function:**
   - Captures the colors from the webcam feed and maps them to the corresponding face of the Rubik's Cube. The captured colors are displayed on a blank image, simulating the Rubik's Cube faces.

4. **capture_sides Function:**
   - Captures and stores the colors for each side of the Rubik's Cube by processing the webcam feed.

5. **main Function:**
   - Controls the overall process of capturing all six sides of the Rubik's Cube and displaying the results.

### Running the Project

1. **Run the Script:**
   ```bash
   python cam.py
   ```

2. **Instructions:**
   - The program will access your webcam and display a window with a bounding box representing a face of the Rubik's Cube.
   - Place the Rubik's Cube face within the bounding box and press the spacebar to capture the face's colors.
   - Repeat this process for all six faces of the cube.
   - After capturing all faces, the program will display a 2D representation of the cube.
   - Press the spacebar again to view the 2D representation.
   - Press `q` to quit.

### Notes

- The color detection logic is based on basic RGB thresholding. Depending on lighting conditions and the quality of the webcam, color detection accuracy might vary.
- The Kociemba algorithm for solving the Rubik's Cube is imported but not integrated into the current version of the code.

### Future Enhancements

- **Improve Color Detection:** Implement more robust color detection techniques, perhaps using machine learning models.
- **Rubik's Cube Solver:** Integrate the Kociemba algorithm to solve the Rubik's Cube based on the detected colors.
- **User Interface:** Develop a graphical user interface to make the project more user-friendly.
