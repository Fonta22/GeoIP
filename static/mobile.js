// Adapt margins properly when the application is run in a mobile browser

/**
 * Regular expression. Returns true if the application is running in a mobile device
 */
const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);

const detailsTable = document.getElementById('details-table');
const mapContainer = document.getElementById('map');
const searchForm = document.getElementById('search-form');

if (isMobile) {
    // Adjust margins
    detailsTable.classList.remove('w-50');
    mapContainer.classList.remove('w-50');
    searchForm.classList.remove('w-50');
}