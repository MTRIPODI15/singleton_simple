import requests

class APIClientSingleton:
    """
    Patrón Singleton para asegurar una única instancia del cliente HTTP 
    (requests.Session) para optimizar recursos en las pruebas.
    """
    _instance = None # Variable de clase para la instancia única
    
    # ------------------------------------------------------------------------
    # 1. Método __new__ para controlar la creación de la instancia
    # ------------------------------------------------------------------------
    def __new__(cls, base_url="https://jsonplaceholder.typicode.com"):
        if cls._instance is None:
            print("\n[SINGLETON] Inicializando NUEVA instancia de APIClient...")
            
            # Crea la instancia y la inicializa
            cls._instance = super(APIClientSingleton, cls).__new__(cls)
            
            # Recursos Costosos: La sesión se crea SÓLO aquí
            cls._instance.base_url = base_url
            cls._instance.session = requests.Session()
            
            # Opcional: Establecer un encabezado de autenticación único si existiera
            # cls._instance.session.headers.update({'Authorization': 'Bearer XXXXXX'})
            
        return cls._instance

    # ------------------------------------------------------------------------
    # 2. Métodos de acceso al recurso (la sesión compartida)
    # ------------------------------------------------------------------------
    def get(self, endpoint):
        """Método GET que usa la sesión única."""
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url)
    
    def get_session_id(self):
        """Retorna el ID de la instancia en memoria para verificación."""
        return id(self)