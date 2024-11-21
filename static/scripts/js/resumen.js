document.addEventListener('DOMContentLoaded', () => {
    loadCartSummary();
    loadCustomerInfo();
    loadPaymentMethod();

    document.getElementById('pay-button').addEventListener('click', processPayment);
});

function loadCartSummary() {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    const cartItemsContainer = document.getElementById('cart-items');
    const cartTotalElement = document.getElementById('cart-total');
    let total = 0;

    cartItemsContainer.innerHTML = '';
    cart.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.classList.add('cart-item');
        itemElement.innerHTML = `
            <span>${item.name} - Talla: ${item.size}, Cantidad: ${item.quantity}</span>
            <span>$${(item.price * item.quantity).toFixed(2)}</span>
        `;
        cartItemsContainer.appendChild(itemElement);
        total += item.price * item.quantity;
    });

    cartTotalElement.textContent = total.toFixed(2);
}

function loadCustomerInfo() {
    const userInfo = JSON.parse(localStorage.getItem('userInfo')) || {};
    const customerDetailsElement = document.getElementById('customer-details');

    customerDetailsElement.innerHTML = `
        <p><strong>Nombre:</strong> ${userInfo.name || 'No especificado'}</p>
        <p><strong>Email:</strong> ${userInfo.email || 'No especificado'}</p>
        <p><strong>Teléfono:</strong> ${userInfo.phone || 'No especificado'}</p>
        <p><strong>Dirección:</strong> ${userInfo.street || 'No especificada'}, ${userInfo.city || ''}, ${userInfo.state || ''} ${userInfo.zip || ''}</p>
    `;
}

function loadPaymentMethod() {
    const userInfo = JSON.parse(localStorage.getItem('userInfo')) || {};
    const paymentMethodElement = document.getElementById('payment-method');

    paymentMethodElement.textContent = userInfo.paymentMethod || 'No especificado';
}

function processPayment() {
    // Aquí iría la lógica real para procesar el pago
    // Por ahora, solo simularemos un pago exitoso

    // Ocultar el resumen y mostrar el mensaje de éxito
    document.getElementById('resumen-container').classList.add('hidden');
    document.getElementById('success-message').classList.remove('hidden');

    // Limpiar el carrito
    localStorage.removeItem('cart');
}