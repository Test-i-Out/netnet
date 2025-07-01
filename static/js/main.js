// Auto-hide messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.message');
    
    messages.forEach(function(message) {
        setTimeout(function() {
            message.style.animation = 'slideOut 0.3s ease-out forwards';
            setTimeout(function() {
                message.remove();
            }, 300);
        }, 5000);
    });

    // Add click functionality to example queries
    const exampleCodes = document.querySelectorAll('.example-code');
    const queryInput = document.querySelector('.query-input');
    
    exampleCodes.forEach(function(code) {
        code.style.cursor = 'pointer';
        code.addEventListener('click', function() {
            const exampleText = this.textContent.trim();
            if (queryInput) {
                queryInput.value = exampleText;
                queryInput.focus();
            }
        });
    });
});

// Add slideOut animation
const styleSheet = document.createElement('style');
styleSheet.textContent = `
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(styleSheet);