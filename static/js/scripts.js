
const marquee = document.getElementById('marquee');

marquee.addEventListener('mouseover', () => {
    marquee.style.animationPlayState = 'paused';
});

marquee.addEventListener('mouseout', () => {
    marquee.style.animationPlayState = 'running';
});
