/**
 * Source AI Web Application - Main JavaScript
 * Handles common functionality across all pages
 */

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    initParticles();
    initTabs();
    initDarkMode();
    initScrollToTop();
    initNotifications();
});

/**
 * Initialize particles background
 */
function initParticles() {
    const particles = document.getElementById('particles');
    if (!particles) return;
    
    const particleCount = 80;
    
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.width = (2 + Math.random() * 4) + 'px';
        particle.style.height = particle.style.width;
        particle.style.animationDelay = Math.random() * 20 + 's';
        particle.style.animationDuration = (15 + Math.random() * 15) + 's';
        
        const colors = ['var(--primary)', 'var(--secondary)', 'var(--accent)', '#ffffff'];
        particle.style.background = colors[Math.floor(Math.random() * colors.length)];
        particle.style.opacity = 0.4 + Math.random() * 0.6;
        
        particles.appendChild(particle);
    }
}

/**
 * Initialize tabs
 */
function initTabs() {
    const tabs = document.querySelectorAll('.tab');
    const contents = document.querySelectorAll('.tab-content');
    
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const target = tab.getAttribute('data-tab');
            
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            
            contents.forEach(c => {
                if (c.id === target) {
                    c.classList.add('active');
                } else {
                    c.classList.remove('active');
                }
            });
        });
    });
}

/**
 * Initialize dark mode toggle
 */
function initDarkMode() {
    const toggle = document.querySelector('.dark-mode-toggle');
    if (!toggle) return;
    
    const button = toggle.querySelector('button');
    const icon = button.innerHTML;
    
    // Check for saved preference
    const prefersDark = localStorage.getItem('prefersDark') === 'true' || 
                        (localStorage.getItem('prefersDark') === null && 
                         window.matchMedia('(prefers-color-scheme: dark)').matches);
    
    if (prefersDark) {
        document.body.classList.add('dark-mode');
        button.innerHTML = '&#9728;&#65039;';
    } else {
        button.innerHTML = '&#127757;';
    }
    
    button.addEventListener('click', () => {
        const isDark = document.body.classList.toggle('dark-mode');
        localStorage.setItem('prefersDark', isDark);
        button.innerHTML = isDark ? '&#9728;&#65039;' : '&#127757;';
    });
}

/**
 * Initialize scroll to top button
 */
function initScrollToTop() {
    const scrollToTop = document.querySelector('.scroll-to-top');
    if (!scrollToTop) return;
    
    const button = scrollToTop.querySelector('button');
    
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            scrollToTop.style.display = 'block';
        } else {
            scrollToTop.style.display = 'none';
        }
    });
    
    button.addEventListener('click', () => {
        window.scrollTo({top: 0, behavior: 'smooth'});
    });
}

/**
 * Initialize notification system
 */
function initNotifications() {
    const container = document.createElement('div');
    container.className = 'notification-container';
    document.body.appendChild(container);
    
    window.showNotification = (message, type = 'info', duration = 5000) => {
        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.innerHTML = `<span>${getNotificationIcon(type)}</span><span>${message}</span>`;
        container.appendChild(notification);
        
        // Remove after duration
        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease-out';
            setTimeout(() => notification.remove(), 300);
        }, duration);
    };
}

/**
 * Get notification icon
 */
function getNotificationIcon(type) {
    const icons = {
        success: '&#10003;',
        warning: '&#9888;',
        error: '&#10007;',
        info: '&#8505;'
    };
    return icons[type] || '&#8505;';
}

/**
 * Show modal
 */
function openModal(title, content) {
    const modal = document.getElementById('modal');
    const modalTitle = document.getElementById('modal-title');
    const modalBody = document.getElementById('modal-body');
    
    if (modal && modalTitle && modalBody) {
        modalTitle.textContent = title;
        modalBody.innerHTML = content;
        modal.classList.add('active');
    }
}

/**
 * Close modal
 */
function closeModal() {
    const modal = document.getElementById('modal');
    if (modal) {
        modal.classList.remove('active');
    }
}

/**
 * Format date
 */
function formatDate(dateString) {
    const options = { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' };
    return new Date(dateString).toLocaleDateString(undefined, options);
}

/**
 * Copy text to clipboard
 */
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showNotification('Copied to clipboard!', 'success');
    }).catch(err => {
        showNotification('Failed to copy', 'error');
        console.error('Failed to copy: ', err);
    });
}

/**
 * Debounce function
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Throttle function
 */
function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

/**
 * Check if element is in viewport
 */
function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

/**
 * Animate element on scroll
 */
function animateOnScroll() {
    const elements = document.querySelectorAll('.slide-up, .fade-in');
    
    elements.forEach(element => {
        if (isInViewport(element)) {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }
    });
}

// Add scroll event listener
window.addEventListener('scroll', throttle(animateOnScroll, 100));

// Initial check
animateOnScroll();

/**
 * Local storage utilities
 */
const Storage = {
    get: (key, defaultValue = null) => {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : defaultValue;
        } catch (e) {
            return defaultValue;
        }
    },
    set: (key, value) => {
        try {
            localStorage.setItem(key, JSON.stringify(value));
            return true;
        } catch (e) {
            return false;
        }
    },
    remove: (key) => {
        try {
            localStorage.removeItem(key);
            return true;
        } catch (e) {
            return false;
        }
    }
};

/**
 * Session storage utilities
 */
const Session = {
    get: (key, defaultValue = null) => {
        try {
            const item = sessionStorage.getItem(key);
            return item ? JSON.parse(item) : defaultValue;
        } catch (e) {
            return defaultValue;
        }
    },
    set: (key, value) => {
        try {
            sessionStorage.setItem(key, JSON.stringify(value));
            return true;
        } catch (e) {
            return false;
        }
    },
    remove: (key) => {
        try {
            sessionStorage.removeItem(key);
            return true;
        } catch (e) {
            return false;
        }
    }
};

/**
 * Cookie utilities
 */
const Cookie = {
    get: (name) => {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
    },
    set: (name, value, days = 7) => {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = `expires=${date.toUTCString()}`;
        document.cookie = `${name}=${value};${expires};path=/`;
        return true;
    },
    remove: (name) => {
        document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/`;
        return true;
    }
};

/**
 * Export utilities
 */
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        initParticles,
        initTabs,
        initDarkMode,
        initScrollToTop,
        initNotifications,
        openModal,
        closeModal,
        formatDate,
        copyToClipboard,
        debounce,
        throttle,
        isInViewport,
        Storage,
        Session,
        Cookie
    };
}