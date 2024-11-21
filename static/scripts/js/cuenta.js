document.addEventListener('DOMContentLoaded', () => {
    loadUserInfo();
    
    document.getElementById('personal-info-form').addEventListener('submit', savePersonalInfo);
    document.getElementById('address-form').addEventListener('submit', saveAddress);
    document.getElementById('payment-method-form').addEventListener('submit', savePaymentMethod);
});

function loadUserInfo() {
    // En una aplicación real, aquí cargarías la información del usuario desde el servidor
    const userInfo = JSON.parse(localStorage.getItem('userInfo')) || {};
    
    document.getElementById('name').value = userInfo.name || '';
    document.getElementById('email').value = userInfo.email || '';
    document.getElementById('phone').value = userInfo.phone || '';
    
    document.getElementById('street').value = userInfo.street || '';
    document.getElementById('city').value = userInfo.city || '';
    document.getElementById('state').value = userInfo.state || '';
    document.getElementById('zip').value = userInfo.zip || '';
    
    // No cargamos la información de la tarjeta por razones de seguridad
    loadPaymentMethod();
}

function savePersonalInfo(e) {
    e.preventDefault();
    const userInfo = JSON.parse(localStorage.getItem('userInfo')) || {};
    
    userInfo.name = document.getElementById('name').value;
    userInfo.email = document.getElementById('email').value;
    userInfo.phone = document.getElementById('phone').value;
    
    localStorage.setItem('userInfo', JSON.stringify(userInfo));
    alert('Información personal guardada');
}

function saveAddress(e) {
    e.preventDefault();
    const userInfo = JSON.parse(localStorage.getItem('userInfo')) || {};
    
    userInfo.street = document.getElementById('street').value;
    userInfo.city = document.getElementById('city').value;
    userInfo.state = document.getElementById('state').value;
    userInfo.zip = document.getElementById('zip').value;
    
    localStorage.setItem('userInfo', JSON.stringify(userInfo));
    alert('Dirección guardada');
}

function savePaymentMethod(e) {
    e.preventDefault();
    const selectedMethod = document.querySelector('input[name="payment-method"]:checked');
    if (selectedMethod) {
        const userInfo = JSON.parse(localStorage.getItem('userInfo')) || {};
        userInfo.paymentMethod = selectedMethod.value;
        localStorage.setItem('userInfo', JSON.stringify(userInfo));
        alert('Método de pago guardado: ' + selectedMethod.value);
    } else {
        alert('Por favor, seleccione un método de pago');
    }
}

function loadPaymentMethod() {
    const userInfo = JSON.parse(localStorage.getItem('userInfo')) || {};
    if (userInfo.paymentMethod) {
        const radioButton = document.querySelector(`input[name="payment-method"][value="${userInfo.paymentMethod}"]`);
        if (radioButton) {
            radioButton.checked = true;
        }
    }
}