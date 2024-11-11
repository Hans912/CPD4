document.querySelectorAll('img').forEach(img => {
    img.onerror = function() {
    this.onerror = null; // Prevents infinite loop if default image missing
    this.src = '../images/default_image.jpg';
    this.alt = ""
    };
    });


document.querySelectorAll('#light').forEach(anchor => {
    const imgUrl = anchor.href; // Get the href attribute of the anchor
    const testImage = new Image();
    testImage.src = imgUrl;

    testImage.onerror = function() {
        console.log("Image not found, setting default image.");
        anchor.href = '../images/default_image.jpg'; // Set default image link
    };
});