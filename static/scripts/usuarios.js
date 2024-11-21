document.addEventListener('DOMContentLoaded', function() {
    const listaUsuarios = document.getElementById('listaUsuarios');
    let intervalId; // Variable para almacenar el ID del intervalo

    async function cargarUsuarios() {
        try {
            const response = await fetch('/api/usuarios');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const usuarios = await response.json();

            // Crear fragmento para mejor rendimiento
            const fragment = document.createDocumentFragment();
            
            usuarios.forEach(usuario => {
                const li = document.createElement('li');
                li.className = 'list-group-item';
                li.textContent = `${usuario.nombreCompleto} - ${usuario.email}`;
                fragment.appendChild(li);
            });

            listaUsuarios.innerHTML = '';
            listaUsuarios.appendChild(fragment);
        } catch (error) {
            console.log('Error al cargar usuarios:', error);
            // Mostrar mensaje de error al usuario
            listaUsuarios.innerHTML = '<li class="list-group-item text-danger">Error al cargar los usuarios</li>';
        }
    }

    // Cargar usuarios al iniciar
    cargarUsuarios();

    // Limpiar el intervalo anterior si existe
    if (intervalId) clearInterval(intervalId);
    intervalId = setInterval(cargarUsuarios, 5000);

    // Limpiar el intervalo cuando la página se oculta
    document.addEventListener('visibilitychange', () => {
        if (document.hidden) {
            clearInterval(intervalId);
        } else {
            intervalId = setInterval(cargarUsuarios, 5000);
        }
    });
});
