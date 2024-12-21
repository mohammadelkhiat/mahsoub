document.addEventListener('DOMContentLoaded', function() {
    fetch('/exercise-data')  // Make sure this endpoint returns the correct data
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById('exerciseChart').getContext('2d');
            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.labels, // Expecting 'labels' from data
                    datasets: [{
                        label: 'Weekly Exercise',
                        data: data.datasets, // Expecting 'datasets' from data
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error loading the chart data:', error));
});
