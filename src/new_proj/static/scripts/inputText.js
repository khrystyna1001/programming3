document.addEventListener('input', function(e) {
    if (e.target.classList.contains('text-block')) {
        const hiddenInput = e.target.querySelector('input[name="content"]');
        if (hiddenInput) {
            hiddenInput.value = e.target.innerText;
        }
    }
});
