document.addEventListener('DOMContentLoaded', function() {
    const inputs = document.querySelectorAll('input');

    inputs.forEach(input => {
        input.addEventListener('blur', function(event) {
            if (!event.target.value) {
                event.target.classList.add('error');
                event.target.nextElementSibling.textContent = 'This field cannot be empty';
            } else {
                event.target.classList.remove('error');
                event.target.nextElementSibling.textContent = '';
            }
        });
    });
});
