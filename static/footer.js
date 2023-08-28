const bodySize = document.querySelector('body').offsetHeight;

// Constantly check the window size to situate the footer right.
setInterval(() => {
    if (bodySize < window.innerHeight) {
        document.getElementById('footer').classList.add('footer');
    } else {
        document.getElementById('footer').classList.remove('footer');
    }
});