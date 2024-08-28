

function openPopup(title, description) {
    document.getElementById('popup-title').innerText = title;
    document.getElementById('popup-description').innerText = description;
    document.getElementById('popup').style.display = 'block';
}

function closePopup() {
    document.getElementById('popup').style.display = 'none';
}
