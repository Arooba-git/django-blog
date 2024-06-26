const titleInput = document.querySelector('input[name=title]');
const slugInput = document.querySelector('input[name=slug]');

function slugify(val) {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')
        .replace(/[\s\W-]+/g, '-')
}

titleInput.addEventListener('keyup', (E) => {
    slugInput.setAttribute('value', slugify(titleInput.value))
});

