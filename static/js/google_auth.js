function handleCredentialResponse(response) {
    console.log("Token recibido de Google. Autenticando...");

    const payload = new FormData();
    payload.append('id_token', response.credential);

    fetch('/usuario/google-login/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': CSRF_TOKEN
        },
        body: payload
    })
    .then(res => res.json())
    .then(data => {
        if (data.status === 'ok') {
            window.location.href = '/'; 
        } else {
            alert("Error al iniciar sesión: " + data.message);
        }
    })
    .catch(error => {
        console.error("Error en la petición:", error);
    });
}