let cart = JSON.parse(localStorage.getItem('cart')) || [];

function displayOrderSummary() {
    const orderSummary = document.getElementById('order-summary');
    let total = 0;

    cart.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.classList.add('summary-item');
        itemElement.innerHTML = `
            <span>${item.name} (${item.size}) x${item.quantity}</span>
            <span>$${(item.price * item.quantity).toFixed(2)}</span>
        `;
        orderSummary.appendChild(itemElement);
        total += item.price * item.quantity;
    });

    const totalElement = document.createElement('div');
    totalElement.classList.add('summary-item');
    totalElement.innerHTML = `
        <strong>Total</strong>
        <strong>$${total.toFixed(2)}</strong>
    `;
    orderSummary.appendChild(totalElement);
}

document.getElementById('payment-form').addEventListener('submit', (e) => {
    e.preventDefault();
    // Aquí deberías implementar la lógica para procesar el pago
    alert('¡Gracias por tu compra!');
    localStorage.removeItem('cart');
    window.location.href = '../index.html';
});

document.addEventListener('DOMContentLoaded', displayOrderSummary);