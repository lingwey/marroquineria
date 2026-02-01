function changeImage(url, element) {
    const mainImg = document.getElementById('main-image');
    
    // Efecto de transición
    mainImg.style.opacity = '0.4';
    
    setTimeout(() => {
        mainImg.src = url;
        mainImg.style.opacity = '1';
    }, 150);

    // Actualizar clase activa en las miniaturas
    document.querySelectorAll('.thumb-item').forEach(img => {
        img.classList.remove('active-thumb');
    });
    element.classList.add('active-thumb');
}
console.log("estoy funcionando")