// Function to handle data deletion
function deleteData(userId) {
    if (confirm('Are you sure you want to delete this data?')) {
        // Send an AJAX request to delete the data
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/delete_data/' + userId, true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
                // Data deleted successfully
                // Reload the page to reflect the changes
                window.location.reload();
            }
        };
        xhr.send();
    }
}


// Add event listeners to all delete buttons
document.querySelectorAll('button[type="submit"]').forEach(function(button) {
    button.addEventListener('click', function(event) {
        // Prevent the default form submission behavior
        event.preventDefault();


        // Extract the user ID from the button's form action attribute
        var userId = button.form.getAttribute('action').split('/').pop();


        // Call the deleteData function with the extracted user ID
        deleteData(userId);
    });
});

