const countdownElement = document.getElementById('countdown');
const messageElement = document.getElementById('message');
const backgroundEffect = document.getElementById('background-effect');

function createStars() {
    for (let i = 0; i < 300; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        const size = Math.random() * 2 + 1;
        star.style.width = `${size}px`;
        star.style.height = `${size}px`;
        star.style.top = `${Math.random() * 100}%`;
        star.style.left = `${Math.random() * 100}%`;
        star.style.animationDuration = `${Math.random() * 3 + 1}s`;
        backgroundEffect.appendChild(star);
    }
}

function createMeteorites() {
    for (let i = 0; i < 10; i++) {
        const meteorite = document.createElement('div');
        meteorite.className = 'meteorite';
        meteorite.style.left = `${Math.random() * 100}%`;
        meteorite.style.animationDelay = `${Math.random() * 5}s`;
        backgroundEffect.appendChild(meteorite);
    }
}

function createComets() {
    for (let i = 0; i < 5; i++) {
        const comet = document.createElement('div');
        comet.className = 'comet';
        comet.style.animationDelay = `${Math.random() * 10}s`;
        backgroundEffect.appendChild(comet);
    }
}

function updateCountdown() {
    const now = new Date();
    const target = new Date('January 1, 2025 00:00:00');
    const timeDiff = target - now;

    if (timeDiff > 0) {
        const hours = Math.floor((timeDiff / (1000 * 60 * 60)) % 24);
        const minutes = Math.floor((timeDiff / (1000 * 60)) % 60);
        const seconds = Math.floor((timeDiff / 1000) % 60);

        countdownElement.textContent = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        messageElement.textContent = 'Countdown to Happy New Year!';
    } else {
        countdownElement.textContent = '00:00:00';
        messageElement.textContent = '🎉 Happy New Year 2025! 🎉 - Bismaya';
    }
}

createStars();
createMeteorites();
createComets();
setInterval(updateCountdown, 1000);