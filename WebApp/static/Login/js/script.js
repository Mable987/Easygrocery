class EcoWellnessLoginForm {
    constructor() {
        this.form = document.getElementById('loginForm');
        this.usernameInput = document.getElementById('username');
        this.passwordInput = document.getElementById('password');
        this.passwordToggle = document.getElementById('passwordToggle');

        this.init();
    }

    init() {
        this.form.addEventListener('submit', (e) => this.handleSubmit(e));
        this.passwordToggle.addEventListener('click', () => this.togglePassword());
    }

    togglePassword() {
        const type = this.passwordInput.type === 'password' ? 'text' : 'password';
        this.passwordInput.type = type;
    }

    validateUsername() {
        const username = this.usernameInput.value.trim();

        if (!username) {
            alert("Username is required");
            return false;
        }
        return true;
    }

    validatePassword() {
        const password = this.passwordInput.value;

        if (!password) {
            alert("Password is required");
            return false;
        }

        if (password.length < 6) {
            alert("Password must be at least 6 characters");
            return false;
        }

        return true;
    }

    handleSubmit(e) {
        const isUsernameValid = this.validateUsername();
        const isPasswordValid = this.validatePassword();

        if (!isUsernameValid || !isPasswordValid) {
            e.preventDefault();   // Stop only if invalid
        }
        // If valid → Django handles login normally
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new EcoWellnessLoginForm();
});