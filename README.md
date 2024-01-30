# Numerical Differentiation Visualizer

This web application, built with Flask, provides an interactive platform to visualize numerical differentiation. It allows users to input a function and select a domain range and step size, then displays graphs of the true differential equation, the FFT (Fast Fourier Transform) approximated function, and the central difference method approximation.

![My Project Screenshot](/assets/showcase.png)

## Features

- **Interactive Input**: Users can input a mathematical function, domain range, and step size.
- **Graphical Representation**: Visualize the true differential equation, FFT approximation, and central difference method on a graph.
- **Flask Backend**: Utilizes Flask, a lightweight Python web framework, for the backend.
- **Easy to Run Locally**: Designed for simple setup and execution on a local machine.

## Prerequisites

- Python 3.x
- Flask
- Additional Python libraries: NumPy, Matplotlib, SciPy (These will be installed via `requirements.txt`).

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/InariHimeko/fft_visual.git
   cd numerical-differentiation-visualizer
2. **Set Up a Python Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Unix or MacOS
   venv\Scripts\activate  # For Windows
3. **Install Dependencies**:
   ```bash
    pip install -r requirements.txt
4. **Running the Application**
   - **Start the Flask Application**:
     ```bash
     python3 app.py
   - **Access the Application**:
     Open a web browser and navigate to [http://127.0.0.1:5000] or [http://localhost:5000].

## Using the Website
1. **Enter a Function**: Input a mathematical function in the provided field (e.g., `sin(x)`, `cos(x) * exp(-x**2)`).
2. **Specify Domain Range and Step/Truncation Size**: Input the start and end values for the domain and specify the step and truncation size for the calculations.
3. **View the Graphs**: After submitting your input, the application will display three plots:
   - The true derivative of the function.
   - The FFT approximated derivative.
   - The central difference method approximation.

## Contributing

Feel free to fork the repository, make improvements or add new features, and submit a pull request. Contributions are welcome!

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask community for the web framework.
- Creators of NumPy, Matplotlib, and SciPy for providing essential scientific computing tools.