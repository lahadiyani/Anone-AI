// script.js

document.getElementById("imageForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Mencegah form dari reload halaman

    const promptInput = document.getElementById("prompt").value;
    const imageContainer = document.getElementById("imageContainer");

    // Tampilkan loading message
    imageContainer.innerHTML = '<p>Loading...</p>';
    fetch('/generate-image', {
        method: 'POST',
        body: new URLSearchParams(new FormData(this)),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok");
        }
        return response.text();
    })
    .then(html => {
        document.open();
        document.write(html);
        document.close();
    })
    .catch(error => {
        imageContainer.innerHTML = '<p class="error">Error: ' + error.message + '</p>';
    });
});
