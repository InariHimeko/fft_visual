# This file is part of fft_visual and is released under the GPL-3.0 License. See LICENSE or https://www.gnu.org/licenses/gpl-3.0.html.
# Author: Wenxuan Xu
# Date: 2024-01-27

from flask import Flask, request, jsonify, render_template
from sympy import symbols, diff, sympify, SympifyError
from sympy.utilities.lambdify import lambdify
from flask_cors import CORS
import numpy as np
from scipy.fft import fft, ifft

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

def calculate_true_derivative(func, x, domain_range, step_size):
    derivative = diff(func, x)
    numerical_derivative = lambdify(x, derivative, 'numpy')
    x_vals = np.arange(domain_range[0], domain_range[1], step_size)
    y_vals = numerical_derivative(x_vals)
    return x_vals.tolist(), y_vals.tolist()

def calculate_fft_derivative(func, x, domain_range, truncation_size):
    num_points = truncation_size
    x_vals_fft = np.linspace(domain_range[0], domain_range[1], num_points)
    y_vals = lambdify(x, func, 'numpy')(x_vals_fft)

    # FFT and spectral derivative
    fhat = fft(y_vals)
    kappa = (2 * np.pi / (domain_range[1] - domain_range[0])) * np.arange(-num_points/2, num_points/2)
    kappa = np.fft.fftshift(kappa)
    dfhat = kappa * fhat * (1j)
    df_vals = np.real(ifft(dfhat))

    return x_vals_fft.tolist(), df_vals.tolist()

def calculate_central_difference_derivative(func, x, domain_range, step_size):
    numerical_func = lambdify(x, func, 'numpy')
    x_vals = np.arange(domain_range[0], domain_range[1], step_size)
    
    # Central Difference: f'(x) ≈ (f(x+h) - f(x-h)) / (2*h)
    y_vals = (numerical_func(x_vals + step_size) - numerical_func(x_vals - step_size)) / (2 * step_size)
    return x_vals.tolist(), y_vals.tolist()


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        func_str = data['function']
        domain_range = data.get('domain_range', [-15, 15])
        step_size = data.get('step_size', 0.1)
        truncation_size = data.get('truncation_size', 400)
        x = symbols('x')
        
        # Safely parse the function string
        func = sympify(func_str, locals={'x': x})

        # Calculate both derivatives
        x_vals_true, true_derivative = calculate_true_derivative(func, x, domain_range, step_size)
        x_vals_fft, fft_derivative = calculate_fft_derivative(func, x, domain_range, truncation_size)
        x_vals_cd, cd_derivative = calculate_central_difference_derivative(func, x, domain_range, step_size)

        response_data = {
            'x_true': x_vals_true,
            'true_derivative': true_derivative,
            'x_fft': x_vals_fft,
            'fft_derivative': fft_derivative,
            'x_cd': x_vals_cd,
            'cd_derivative': cd_derivative
        }
        # print(response_data)
        return jsonify(response_data)
    except SympifyError:
        return jsonify({"error": "Invalid function"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
