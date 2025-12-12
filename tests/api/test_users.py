from src.api_clients.api_client_singleton import APIClientSingleton

# ------------------------------------------------------------------------
# Fixture para acceder al Singleton
# ------------------------------------------------------------------------
# Creamos el cliente aquí, y Pytest lo usará en las pruebas que lo pidan.
# La primera llamada lo inicializará; las siguientes lo devolverán.
API_CLIENT = APIClientSingleton() 
SESSION_ID = API_CLIENT.get_session_id() # Capturamos el ID de la instancia única

def test_fetch_single_user():
    """Prueba A: Verifica que se pueda obtener un recurso, usando la sesión Singleton."""
    
    print(f"\n[TEST A] ID de Sesión: {API_CLIENT.get_session_id()}")
    
    # Usando el método GET de la instancia única
    response = API_CLIENT.get("/users/1") 
    
    assert response.status_code == 200
    assert response.json()["id"] == 1
    # Verificamos que el ID de sesión no haya cambiado
    assert API_CLIENT.get_session_id() == SESSION_ID


def test_fetch_multiple_posts():
    """Prueba B: Consulta otro recurso. Debe seguir usando la MISMA instancia."""
    
    print(f"\n[TEST B] ID de Sesión: {API_CLIENT.get_session_id()}")
    
    # Usando el método GET de la misma instancia
    response = API_CLIENT.get("/posts") 
    
    assert response.status_code == 200
    assert len(response.json()) > 5 # Hay varios posts
    # La prueba clave de Singleton: El ID de sesión DEBE ser el mismo que el original
    assert API_CLIENT.get_session_id() == SESSION_ID