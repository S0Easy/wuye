document.addEventListener('formset:added', (event) => {
    if (event.detail.formsetName == 'author_set') {
        // Do something
    }
});
document.addEventListener('formset:removed', (event) => {
    // Row removed
});