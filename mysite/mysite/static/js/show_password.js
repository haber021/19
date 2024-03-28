document.addEventListener('DOMContentLoaded', function() {
    const submitBtn = document.querySelector(".submit-btn");
    const showPasswordToggle = document.querySelector(".showPasswordToggle");
    const passwordField = document.querySelector("#passwordField");

    const handleToggleInput = (e) => {
        if (showPasswordToggle.textContent === 'SHOW') {
            showPasswordToggle.textContent = 'HIDE';
            passwordField.setAttribute("type", "text");
        } else {
            showPasswordToggle.textContent = 'SHOW';
            passwordField.setAttribute("type", "password");
        }
    };

    if (showPasswordToggle) {
        showPasswordToggle.addEventListener('click', handleToggleInput);
    }
});