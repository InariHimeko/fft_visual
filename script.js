function performCalculation() {
    const functionInput = document.getElementById('functionInput').value;
    const domainStart = parseFloat(document.getElementById('domainStart').value);
    const domainEnd = parseFloat(document.getElementById('domainEnd').value);
    const stepSize = parseFloat(document.getElementById('stepSize').value);

    // Basic validation
    if (!functionInput.trim() || isNaN(domainStart) || isNaN(domainEnd) || isNaN(stepSize)) {
        alert('Please enter valid function, domain range, and step size.');
        return;
    }

    fetch('http://127.0.0.1:5000/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            function: functionInput,
            domain_range: [domainStart, domainEnd],
            step_size: stepSize
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        plotGraph(data);
    })
    .catch(error => {
        console.error('Error during fetch operation:', error);
        alert('An error occurred: ' + error.message);
    });
}

function plotGraph(data) {
    const trueDerivativeTrace = {
        x: data.x_true,
        y: data.true_derivative,
        mode: 'lines',
        type: 'scatter',
        name: 'True Derivative'
    };

    const fftDerivativeTrace = {
        x: data.x_fft,
        y: data.fft_derivative,
        mode: 'lines',
        type: 'scatter',
        name: 'FFT Derivative'
    };

    const cdDerivativeTrace = {
        x: data.x_cd,
        y: data.cd_derivative,
        mode: 'lines',
        type: 'scatter',
        name: 'Central Difference Derivative',
        line: { dash: 'dash' }
    };

    const layout = {
        title: 'Function Derivatives',
        xaxis: { title: 'x' },
        yaxis: { title: 'F\'(x)' },
        height: 600
    };

    Plotly.newPlot('graph', [trueDerivativeTrace, fftDerivativeTrace, cdDerivativeTrace], layout);
}

