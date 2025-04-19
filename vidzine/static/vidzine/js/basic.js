// Basic JavaScript for Vidzine App

document.addEventListener('DOMContentLoaded', function() {
    console.log('Vidzine App Loaded');
    
    // Add event listeners to any interactive elements
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            console.log('Button clicked:', this.textContent);
        });
    });
    
    // Function to toggle visibility of elements
    window.toggleElement = function(elementId) {
        const element = document.getElementById(elementId);
        if (element) {
            if (element.style.display === 'none' || element.style.display === '') {
                element.style.display = 'block';
            } else {
                element.style.display = 'none';
            }
        }
    };
    
    // Simple animation for page elements
    const headerElement = document.querySelector('.header');
    if (headerElement) {
        headerElement.style.opacity = '0';
        setTimeout(() => {
            headerElement.style.transition = 'opacity 0.5s ease-in-out';
            headerElement.style.opacity = '1';
        }, 100);
    }
}); 