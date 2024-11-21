let cart = JSON.parse(localStorage.getItem('cart')) || [];

function displayCart() {
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    
    cartItems.innerHTML = '';
    let total = 0;

    cart.forEach((item, index) => {
        const itemElement = document.createElement('div');
        itemElement.classList.add('cart-item');
        itemElement.innerHTML = `
            <div class="cart-item-info">
                <h3 class="cart-item-name">${item.name}</h3>
                <p class="cart-item-price">$${item.price.toFixed(2)}</p>
                <p>Talla: ${item.size}, Cantidad: ${item.quantity}</p>
            </div>
            <button class="remove-item" onclick="removeItem(${index})">Eliminar</button>
        `;
        cartItems.appendChild(itemElement);
        total += item.price * item.quantity;
    });

    cartTotal.textContent = total.toFixed(2);
    localStorage.setItem('cart', JSON.stringify(cart));
}

function removeItem(index) {
    cart.splice(index, 1);
    localStorage.setItem('cart', JSON.stringify(cart));
    displayCart();
    updateCartCount();
}

function updateCartCount() {
    const cartCount = document.getElementById('cart-count');
    if (cartCount) {
        cartCount.textContent = cart.reduce((total, item) => total + item.quantity, 0);
    }
}

document.getElementById('checkout').addEventListener('click', () => {
    window.location.href = 'resumen.html';
});

document.addEventListener('DOMContentLoaded', () => {
    displayCart();
    updateCartCount();
});