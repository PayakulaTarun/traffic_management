// traffic-alert.js

// Function to simulate checking traffic conditions
function checkTrafficConditions() {
    // Simulate a random traffic condition (for demonstration purposes)
    const trafficLevel = Math.random(); // Random value between 0 and 1

    // Define a threshold for high traffic (e.g., 0.7)
    const highTrafficThreshold = 0.7;

    if (trafficLevel > highTrafficThreshold) {
        alert("Alert: High traffic detected! Please consider alternate routes.");
    } else {
        console.log("Traffic is normal.");
    }
}

// Call the function to check traffic conditions when the page loads
window.onload = function() {
    checkTrafficConditions();
};