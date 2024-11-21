// Datos de ejemplo para los productos
const products = [
    { id: 1, name: "Vestido Elegante", price: 199.99, category: "mujer", image: "../../static/images/Top Marie.webp", description: "Un hermoso vestido para ocasiones especiales." },
    { id: 2, name: "Traje Formal", price: 299.99, category: "hombre", image: "../../static/images/Top Marie.webp", description: "Un traje elegante para eventos formales." },
    { id: 3, name: "Conjunto Infantil", price: 79.99, category: "infantil", image: "../../static/images/Top Lido Violeta.webp", description: "Un adorable conjunto para los más pequeños." },
    { id: 4, name: "Conjunto Infantil", price: 79.99, category: "mujer", image: "../../static/images/Top Lido Violeta.webp", description: "Un adorable conjunto para los más pequeños." },
    { id: 5, name: "Conjunto Infantil", price: 79.99, category: "hombre", image: "../../static/images/Top Lido Violeta.webp", description: "Un adorable conjunto para los más pequeños." },
    { id: 6, name: "Blusa Floral", price: 89.99, category: "mujer", image: "../../static/images/Top Marie.webp", description: "Elegante blusa con estampado floral." },
    { id: 7, name: "Falda Midi", price: 129.99, category: "mujer", image: "../../static/images/Top Lido Violeta.webp", description: "Falda midi de corte elegante." },
    { id: 8, name: "Pantalón de Vestir", price: 159.99, category: "mujer", image: "../../static/images/Top Marie.webp", description: "Pantalón formal para ocasiones especiales." },
    { id: 9, name: "Blazer Clásico", price: 199.99, category: "mujer", image: "../../static/images/Top Lido Violeta.webp", description: "Blazer elegante para looks formales." },
    { id: 10, name: "Vestido de Noche", price: 299.99, category: "mujer", image: "../../static/images/Top Marie.webp", description: "Vestido largo para eventos de gala." },
    { id: 11, name: "Camisa Formal", price: 129.99, category: "hombre", image: "../../static/images/Top Lido Violeta.webp", description: "Camisa de vestir de algodón premium." },
    { id: 12, name: "Pantalón Chino", price: 149.99, category: "hombre", image: "../../static/images/Top Marie.webp", description: "Pantalón casual elegante." },
    { id: 13, name: "Saco Sport", price: 249.99, category: "hombre", image: "../../static/images/Top Lido Violeta.webp", description: "Saco versátil para ocasiones casuales." },
    { id: 14, name: "Chaleco Formal", price: 179.99, category: "hombre", image: "../../static/images/Top Marie.webp", description: "Chaleco elegante para trajes." },
    { id: 15, name: "Smoking", price: 399.99, category: "hombre", image: "../../static/images/Top Lido Violeta.webp", description: "Smoking clásico para eventos formales." },
    { id: 16, name: "Vestido Infantil", price: 89.99, category: "infantil", image: "../../static/images/Top Marie.webp", description: "Vestido elegante para niñas." },
    { id: 17, name: "Traje Junior", price: 159.99, category: "infantil", image: "../../static/images/Top Lido Violeta.webp", description: "Traje formal para niños." },
    { id: 18, name: "Conjunto Deportivo", price: 69.99, category: "infantil", image: "../../static/images/Top Marie.webp", description: "Conjunto deportivo cómodo para niños." },
    { id: 19, name: "Pijama Infantil", price: 49.99, category: "infantil", image: "../../static/images/Top Lido Violeta.webp", description: "Pijama suave y cómoda para niños." },
    { id: 20, name: "Abrigo Infantil", price: 129.99, category: "infantil", image: "../../static/images/Top Marie.webp", description: "Abrigo abrigado para niños." }
];

let cart = [];

// Función para mostrar los productos en la página
function displayProducts(category = null) {
    const productsGrid = document.getElementById('products-grid');
    productsGrid.innerHTML = '';

    const filteredProducts = category ? products.filter(p => p.category === category) : products;

    filteredProducts.forEach(product => {
        const productElement = document.createElement('div');
        productElement.classList.add('product-card');
        productElement.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <div class="product-info">
                <h3 class="product-name">${product.name}</h3>
                <p class="product-price">$${product.price.toFixed(2)}</p>
                <button onclick="openProductModal(${product.id})">Ver detalles</button>
            </div>
        `;
        productsGrid.appendChild(productElement);
    });
}

// Función para abrir el modal de producto
function openProductModal(productId) {
    const product = products.find(p => p.id === productId);
    const modal = document.getElementById('product-modal');
    document.getElementById('modal-product-name').textContent = product.name;
    document.getElementById('modal-product-price').textContent = `$${product.price.toFixed(2)}`;
    document.getElementById('modal-product-description').textContent = product.description;
    document.getElementById('add-to-cart').onclick = () => addToCart(product);
    document.getElementById('product-image').setAttribute('src', product.image)
    modal.style.display = 'block';
}

// Función para cerrar los modales
function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Función para agregar un producto al carrito
function addToCart(product) {
    const size = document.getElementById('modal-product-size').value;
    const quantity = parseInt(document.getElementById('modal-product-quantity').value);
    cart.push({ ...product, size, quantity });
    updateCartCount();
    closeModal('product-modal');
}

// Función para actualizar el contador del carrito
function updateCartCount() {
    document.getElementById('cart-count').textContent = cart.length;
}

// Función para mostrar el carrito
function showCart() {
    const cartItems = document.getElementById('cart-items');
    cartItems.innerHTML = '';
    let total = 0;

    cart.forEach((item, index) => {
        const itemElement = document.createElement('div');
        itemElement.innerHTML = `
            <p>${item.name} - Talla: ${item.size} - Cantidad: ${item.quantity} - $${(item.price * item.quantity).toFixed(2)}</p>
            <button onclick="removeFromCart(${index})">Eliminar</button>
        `;
        cartItems.appendChild(itemElement);
        total += item.price * item.quantity;
    });

    document.getElementById('cart-total').textContent = total.toFixed(2);
    document.getElementById('cart-modal').style.display = 'block';
}

// Función para eliminar un producto del carrito
function removeFromCart(index) {
    cart.splice(index, 1);
    updateCartCount();
    showCart();
}

// Event Listeners
document.addEventListener('DOMContentLoaded', () => {
    displayProducts();

    // Cerrar modales
    document.querySelectorAll('.close').forEach(closeBtn => {
        closeBtn.onclick = () => closeModal(closeBtn.closest('.modal').id);
    });

    // Filtrar productos por categoría
    document.querySelectorAll('.dropdown-content a').forEach(link => {
        link.onclick = (e) => {
            e.preventDefault();
            displayProducts(link.dataset.category);
        };
    });

    // Mostrar carrito
    document.getElementById('cart-icon').onclick = showCart;

    // Proceder al pago
    /*     document.getElementById('checkout').onclick = () => {
            // Aquí iría la lógica para redirigir a la página de pago
            alert('Redirigiendo a la página de pago...');
        }; */
});