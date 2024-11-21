// Obtener la categoría de la URL
const urlParams = new URLSearchParams(window.location.search);
const category = urlParams.get('category');

// Función para cargar los productos de la categoría
function loadCategoryProducts() {
    const categoryTitle = document.getElementById('category-title');
    const categoryProducts = document.getElementById('category-products');

    categoryTitle.textContent = category.charAt(0).toUpperCase() + category.slice(1);

    // Aquí deberías hacer una llamada a tu API para obtener los productos de la categoría
    // Por ahora, usaremos datos de ejemplo
    const products = Array.from({ length: 20 }, (_, i) => ({
        id: i + 1,
        name: `Producto ${i + 1}`,
        price: (Math.random() * 100 + 50).toFixed(2),
        image: `../img/producto${(i % 5) + 1}.jpg` // Asumimos que tienes 5 imágenes de ejemplo
    }));

    products.forEach(product => {
        const productElement = document.createElement('div');
        productElement.classList.add('product-card');
        productElement.innerHTML = `
            <img src="${product.image}" alt="${product.name}" onclick="openProductModal(${product.id})">
            <div class="product-info">
                <h3 class="product-name">${product.name}</h3>
                <p class="product-price">$${product.price}</p>
                <button onclick="addToCart(${product.id})" class="button">Agregar al carrito</button>
            </div>
        `;
        categoryProducts.appendChild(productElement);
    });
}

function openProductModal(productId) {
    // Aquí implementarías la lógica para abrir un modal con los detalles del producto
    alert(`Abriendo detalles del producto ${productId}`);
}

function addToCart(productId) {
    // Aquí implementarías la lógica para agregar el producto al carrito
    alert(`Producto ${productId} añadido al carrito`);
}

document.addEventListener('DOMContentLoaded', loadCategoryProducts);