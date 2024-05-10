function changeTextColor() {
    var element = document.getElementById('text');
    if (element.style.color == 'red') {
        element.style.color = 'black';
    } else {
        element.style.color = 'red';
    }
}

function showAlert() {
    alert('This is an example script!');
}