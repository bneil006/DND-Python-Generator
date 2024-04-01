document.getElementById('moduleForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Retrieve the form values
    const brand = document.getElementById('brandSelect').value;
    const watt = document.getElementById('wattInput').value;
    const panelCount = document.getElementById('panelCountInput').value;
    const roofSize = document.getElementById('roofSizeInput').value;

    // Fetch the design result
    fetch(`/design_result?brand=${encodeURIComponent(brand)}&watt=${encodeURIComponent(watt)}&panel_count=${encodeURIComponent(panelCount)}&roof_size=${encodeURIComponent(roofSize)}`)
        .then(response => response.json()) // Parse the JSON response
        .then(data => {
            if (data.error) {
                // If there is an error in the response, display it
                document.getElementById('result').innerHTML = `<span style="color: red;">Error: ${data.error}</span>`;
            } else {
                // Display the result without the JSON structure, directly showing the string
                document.getElementById('result').innerHTML = data.result;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('result').innerHTML = `<span style="color: red;">An unexpected error occurred.</span>`;
        });
});
