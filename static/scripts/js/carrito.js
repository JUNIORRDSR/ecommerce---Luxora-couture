let cart = JSON.parse(localStorage.getItem('cart')) || [];

function displayCart() {
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    const emptyCartMessage = document.getElementById('empty-cart-message');

    cartItems.innerHTML = '';
    let total = 0;

    if (cart.length === 0) {
        cartItems.innerHTML = '<p class="empty-cart">Tu carrito está vacío</p>';
        cartTotal.textContent = '0.00';
        if (emptyCartMessage) emptyCartMessage.style.display = 'block';
        document.getElementById('checkout').style.display = 'none';
        return;
    }

    cart.forEach((item, index) => {
        const itemElement = document.createElement('div');
        itemElement.classList.add('cart-item');
        itemElement.innerHTML = `
            <div class="cart-item-info">
                <img src="${item.image}" alt="${item.name}" class="cart-item-image">
                <div class="cart-item-details">
                    <h3 class="cart-item-name">${item.name}</h3>
                    <p class="cart-item-price">$${item.price.toFixed(2)}</p>
                    <div class="cart-item-controls">
                        <label>Talla: 
                            <select class="size-select" onchange="updateItemSize(${index}, this.value)">
                                ${generateSizeOptions(item.size)}
                            </select>
                        </label>
                        <label>Cantidad: 
                            <input type="number" 
                                   value="${item.quantity}" 
                                   min="1" 
                                   max="10" 
                                   class="quantity-input"
                                   onchange="updateItemQuantity(${index}, this.value)">
                        </label>
                    </div>
                    <p class="item-subtotal">Subtotal: $${(item.price * item.quantity).toFixed(2)}</p>
                </div>
            </div>
            <button class="remove-item" onclick="removeItem(${index})">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18"/><path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"/><path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"/></svg>
            </button>
        `;
        cartItems.appendChild(itemElement);
        total += item.price * item.quantity;
    });

    cartTotal.textContent = total.toFixed(2);
    document.getElementById('checkout').style.display = 'block';
    if (emptyCartMessage) emptyCartMessage.style.display = 'none';
}

function generateSizeOptions(selectedSize) {
    const sizes = ['XS', 'S', 'M', 'L', 'XL'];
    return sizes.map(size =>
        `<option value="${size}" ${size === selectedSize ? 'selected' : ''}>${size}</option>`
    ).join('');
}

function updateItemSize(index, newSize) {
    cart[index].size = newSize;
    saveCartAndUpdate();
}

function updateItemQuantity(index, newQuantity) {
    newQuantity = parseInt(newQuantity);
    if (newQuantity < 1) newQuantity = 1;
    if (newQuantity > 10) newQuantity = 10;

    cart[index].quantity = newQuantity;
    saveCartAndUpdate();
}

function removeItem(index) {
    if (confirm('¿Estás seguro de que deseas eliminar este artículo?')) {
        cart.splice(index, 1);
        saveCartAndUpdate();
    }
}

function saveCartAndUpdate() {
    localStorage.setItem('cart', JSON.stringify(cart));
    displayCart();
}

function proceedToCheckout() {
    if (cart.length === 0) {
        alert('Tu carrito está vacío');
        return;
    }
    window.location.href = '../templates/pages/html/pago.html';
}

// Event Listeners
document.addEventListener('DOMContentLoaded', () => {
    displayCart();

    const checkoutButton = document.getElementById('checkout');
    if (checkoutButton) {
        checkoutButton.addEventListener('click', proceedToCheckout);
    }

    // Botón para vaciar carrito
    const clearCartButton = document.getElementById('clear-cart');
    if (clearCartButton) {
        clearCartButton.addEventListener('click', () => {
            if (confirm('¿Estás seguro de que deseas vaciar el carrito?')) {
                cart = [];
                saveCartAndUpdate();
            }
        });
    }
});

// Función para actualizar el carrito desde otras páginas
function updateCartFromModal(updatedCart) {
    cart = updatedCart;
    saveCartAndUpdate();
}

// Exportar funciones si es necesario
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        cart,
        displayCart,
        updateCartFromModal,
        removeItem,
        updateItemQuantity,
        updateItemSize
    };
}