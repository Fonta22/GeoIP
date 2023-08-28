const loc = document.getElementById('loc').value;
const lat = loc.split(',')[0];
const lon = loc.split(',')[1];

const map = L.map('map').setView([lat, lon], 5);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    minZoom: 2,
    maxZoom: 19,
    attribution: '© OpenStreetMap'
}).addTo(map);

L.marker([lat, lon]).addTo(map);