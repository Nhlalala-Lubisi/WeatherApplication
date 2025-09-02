document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.container');
    container.style.opacity = 0;
    container.style.transform = 'translateY(20px)';
    
    setTimeout(() => {
        container.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        container.style.opacity = 1;
        container.style.transform = 'translateY(0)';
    }, 100);
    
    const input = document.querySelector('input[name="city"]');
    if (input) {
        input.focus();
    }
    
    const form = document.querySelector('.search-form');
    if (form) {
        form.addEventListener('submit', function(e) {
            const button = this.querySelector('button');
            button.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            
            setTimeout(function() {
                button.innerHTML = '<i class="fas fa-arrow-right"></i>';
            }, 2000);
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const body = document.querySelector("body.dynamic-bg");

    if (body && body.dataset.bg) {
        body.style.backgroundImage = `linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('${body.dataset.bg}')`;
    }
});
