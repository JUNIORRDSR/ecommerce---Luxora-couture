document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById('registroForm');
    const mensajeRespuesta = document.getElementById('mensajeRespuesta');

    formulario.addEventListener('submit', async function(e) {
        e.preventDefault();

        const datosUsuario = {
            nombreCompleto: document.getElementById('nombreCompleto').value,
            email: document.getElementById('email').value,
            contraseña: document.getElementById('contraseña').value,
            cedula: document.getElementById('cedula').value,
            telefono: document.getElementById('telefono').value
        };

        try {
            const response = await fetch('/registro', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(datosUsuario)
            });

            const data = await response.json();

            if (response.ok) {
                mensajeRespuesta.innerHTML = `
                    <div class="alert alert-success">
                        Usuario registrado exitosamente
                    </div>
                `;
                formulario.reset();
            } else {
                mensajeRespuesta.innerHTML = `
                    <div class="alert alert-danger">
                        ${data.error || 'Error al registrar usuario'}
                    </div>
                `;
            }
        } catch (error) {
            mensajeRespuesta.innerHTML = `
                <div class="alert alert-danger">
                    Error de conexión: ${error.message}
                </div>
            `;
        }
    });

    // Validación básica de cédula y teléfono
    document.getElementById('cedula').addEventListener('input', function(e) {
        this.value = this.value.replace(/[^0-9]/g, '');
    });

    document.getElementById('telefono').addEventListener('input', function(e) {
        this.value = this.value.replace(/[^0-9]/g, '');
    });
});