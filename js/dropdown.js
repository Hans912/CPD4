document.addEventListener('DOMContentLoaded', () => {
    const dropdown = document.querySelector('.dropdown'); // Dropdown container
    const button = dropdown.querySelector('button');      // Button to open dropdown
    const content = dropdown.querySelector('.dropdown-content'); // Dropdown links

    // Toggle dropdown visibility on button click
    button.addEventListener('click', (event) => {
        event.stopPropagation(); // Prevent click from bubbling up
        content.classList.toggle('visible'); // Toggle visibility class
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', (event) => {
        if (!dropdown.contains(event.target)) {
            content.classList.remove('visible'); // Hide dropdown
        }
    });

    // Reset dropdown state when returning to the homepage
    window.addEventListener('pageshow', (event) => {
        if (event.persisted) {  // Browser cache handling
            content.classList.remove('visible'); // Reset dropdown visibility
        }
    });
});
