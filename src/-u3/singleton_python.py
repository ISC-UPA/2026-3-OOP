import os, sys
import threading
from typing import Optional

# ============================================
# 1. SINGLETON BÁSICO (usando __new__)
# ============================================
class Singleton:
    """
    Implementación básica usando __new__
    Python llama a __new__ antes de __init__
    """
    _instance: Optional['Singleton'] = None
    
    def __new__(cls):
        if cls._instance is None:
            print("Creando nueva instancia de Singleton")
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        # Cuidado: __init__ se llama cada vez que se crea una "nueva" instancia
        print("Llamando a __init__")
    
    def operacion(self):
        print("Ejecutando operación del Singleton")


# ============================================
# 2. SINGLETON CON INICIALIZACIÓN ÚNICA
# ============================================
class SingletonInicializacionUnica:
    """
    Evita que __init__ se ejecute múltiples veces
    """
    _instance: Optional['SingletonInicializacionUnica'] = None
    _inicializado = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not SingletonInicializacionUnica._inicializado:
            print("Inicializando Singleton por primera vez")
            self.valor = "Configuración inicial"
            SingletonInicializacionUnica._inicializado = True
    
    def operacion(self):
        print(f"Operación con valor: {self.valor}")


# ============================================
# 3. SINGLETON THREAD-SAFE (con Lock)
# ============================================
class SingletonThreadSafe:
    """
    Seguro para entornos multihilo
    """
    _instance: Optional['SingletonThreadSafe'] = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # Double-check dentro del lock
                if cls._instance is None:
                    print("Creando instancia thread-safe")
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def operacion(self):
        print("Operación thread-safe")


# ============================================
# 4. SINGLETON CON METACLASE (avanzado)
# ============================================
class SingletonMeta(type):
    """
    Metaclase para crear Singletons automáticamente
    """
    _instances = {}
    _lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class ConfiguracionGlobal(metaclass=SingletonMeta):
    """
    Usar metaclase es la forma más elegante en Python
    """
    def __init__(self):
        print("Inicializando ConfiguracionGlobal")
        self.app_name = "Mi Aplicación"
        self.version = "1.0.0"
        self.debug = True
    
    def mostrar_config(self):
        print(f"App: {self.app_name} v{self.version}")
        print(f"Debug: {self.debug}")


# ============================================
# 5. SINGLETON CON DECORADOR (muy pythonic)
# ============================================
def singleton(clase):
    """
    Decorador para convertir cualquier clase en Singleton
    """
    instancias = {}
    lock = threading.Lock()
    
    def obtener_instancia(*args, **kwargs):
        if clase not in instancias:
            with lock:
                if clase not in instancias:
                    instancias[clase] = clase(*args, **kwargs)
        return instancias[clase]
    
    return obtener_instancia


@singleton
class Logger:
    """
    Logger usando el decorador singleton
    """
    def __init__(self):
        print("Inicializando Logger")
        self.logs = []
    
    def log(self, mensaje: str):
        self.logs.append(mensaje)
        print(f"📝 LOG: {mensaje}")
    
    def mostrar_logs(self):
        print("\n=== Historial de Logs ===")
        for i, log in enumerate(self.logs, 1):
            print(f"{i}. {log}")


# ============================================
# 6. SINGLETON CON MÓDULO (más pythonic)
# ============================================
# En Python, los módulos son singletons naturales
class _DatabaseConnection:
    """
    Clase privada para la conexión
    """
    def __init__(self):
        print("Estableciendo conexión a la base de datos")
        self.connection_string = "postgresql://localhost:5432/mydb"
        self.activa = True
    
    def ejecutar_query(self, sql: str):
        if self.activa:
            print(f"🔍 Ejecutando: {sql}")
            print(f"   En: {self.connection_string}")
        else:
            print("❌ Conexión cerrada")
    
    def cerrar(self):
        self.activa = False
        print("Conexión cerrada")


# Instancia única exportada
database = _DatabaseConnection()


# ============================================
# 7. EJEMPLO PRÁCTICO: Sistema de Configuración
# ============================================
class ConfiguracionApp(metaclass=SingletonMeta):
    """
    Configuración global de la aplicación
    """
    def __init__(self):
        if not hasattr(self, '_inicializado'):
            print("⚙️  Cargando configuración de la aplicación")
            self._inicializado = True
            self.idioma = "es"
            self.tema = "oscuro"
            self.notificaciones = True
            self.configuraciones = {}
    
    def establecer(self, clave: str, valor):
        self.configuraciones[clave] = valor
        print(f"✓ Configuración '{clave}' = {valor}")
    
    def obtener(self, clave: str, default=None):
        return self.configuraciones.get(clave, default)
    
    def mostrar_todas(self):
        print("\n=== Configuración Actual ===")
        print(f"Idioma: {self.idioma}")
        print(f"Tema: {self.tema}")
        print(f"Notificaciones: {self.notificaciones}")
        print(f"Configuraciones personalizadas: {self.configuraciones}")


# ============================================
# 8. ANTI-PATRÓN: Singleton con variable global
# ============================================
# ❌ NO RECOMENDADO pero común en código legacy
_instancia_cache = None

class CacheSingleton:
    def __init__(self):
        global _instancia_cache
        if _instancia_cache is not None:
            raise Exception("¡Solo puede existir una instancia de Cache!")
        _instancia_cache = self
        self.datos = {}
    
    @staticmethod
    def obtener_instancia():
        global _instancia_cache
        if _instancia_cache is None:
            _instancia_cache = CacheSingleton()
        return _instancia_cache


# ============================================
# PRUEBAS Y EJEMPLOS
# ============================================
def test_singleton_basico():
    print("=" * 60)
    print("TEST 1: Singleton Básico")
    print("=" * 60)
    
    s1 = Singleton()
    print(f"ID de s1: {id(s1)}")
    
    s2 = Singleton()
    print(f"ID de s2: {id(s2)}")
    
    print(f"¿Son la misma instancia? {s1 is s2}")
    s1.operacion()


def test_singleton_inicializacion():
    print("\n" + "=" * 60)
    print("TEST 2: Singleton con Inicialización Única")
    print("=" * 60)
    
    s1 = SingletonInicializacionUnica()
    s1.operacion()
    
    s2 = SingletonInicializacionUnica()
    s2.operacion()
    
    print(f"¿Mismo valor? {s1.valor == s2.valor}")


def test_singleton_threadf():
    print("\n" + "=" * 60)
    print("TEST 3: Singleton Thread-Safe")
    print("=" * 60)
    
    def crear_instancia(nombre):
        instancia = SingletonThreadSafe()
        print(f"Hilo {nombre}: ID = {id(instancia)}")
    
    hilos = []
    for i in range(5):
        hilo = threading.Thread(target=crear_instancia, args=(f"T{i}",))
        hilos.append(hilo)
        hilo.start()
    
    for hilo in hilos:
        hilo.join()


def test_metaclase():
    print("\n" + "=" * 60)
    print("TEST 4: Singleton con Metaclase")
    print("=" * 60)
    
    config1 = ConfiguracionGlobal()
    config1.mostrar_config()
    
    config2 = ConfiguracionGlobal()
    print(f"\n¿Son la misma instancia? {config1 is config2}")
    
    config2.debug = False
    print("\nDespués de modificar config2:")
    config1.mostrar_config()


def test_decorador():
    print("\n" + "=" * 60)
    print("TEST 5: Singleton con Decorador")
    print("=" * 60)
    
    logger1 = Logger()
    logger1.log("Primera entrada")
    logger1.log("Segunda entrada")
    
    logger2 = Logger()
    logger2.log("Tercera entrada")
    
    print(f"\n¿Son la misma instancia? {logger1 is logger2}")
    logger1.mostrar_logs()


def test_modulo():
    print("\n" + "=" * 60)
    print("TEST 6: Singleton con Módulo")
    print("=" * 60)
    
    # Usar la instancia del módulo directamente
    database.ejecutar_query("SELECT * FROM usuarios")
    database.ejecutar_query("INSERT INTO logs VALUES ('test')")
    
    # No importa dónde se importe, siempre es la misma instancia
    from __main__ import database as db2
    print(f"\n¿Misma conexión? {database is db2}")


def test_ejemplo_practico():
    print("\n" + "=" * 60)
    print("TEST 7: Ejemplo Práctico - ConfiguracionApp")
    print("=" * 60)
    
    # Primera vez
    config = ConfiguracionApp()
    config.establecer("max_intentos", 3)
    config.establecer("timeout", 30)
    
    # Desde otra parte del código
    config2 = ConfiguracionApp()
    print(f"\n¿Son la misma configuración? {config is config2}")
    print(f"Max intentos desde config2: {config2.obtener('max_intentos')}")
    
    config2.mostrar_todas()


def comparacion_metodos():
    print("\n" + "=" * 60)
    print("COMPARACIÓN: ¿Cuál método usar?")
    print("=" * 60)
    
    print("""
    1️⃣  __new__: Simple pero cuidado con __init__
       ✓ Fácil de entender
       ✗ __init__ se ejecuta múltiples veces
    
    2️⃣  Metaclase: La más elegante y poderosa
       ✓ Muy pythonic
       ✓ Thread-safe
       ✓ Control total
       ✗ Más compleja de entender
    
    3️⃣  Decorador: Balance entre simplicidad y poder
       ✓ Reutilizable
       ✓ Fácil de aplicar
       ✓ Thread-safe
       ⭐ RECOMENDADO para la mayoría de casos
    
    4️⃣  Módulo: Lo más pythonic de todo
       ✓ Extremadamente simple
       ✓ Los módulos son singletons naturales
       ⭐ RECOMENDADO cuando no necesitas lazy loading
    """)


# ============================================
# MAIN
# ============================================
if __name__ == "__main__":
    os.system("cls")
    test_singleton_basico()
    test_singleton_inicializacion()
    test_singleton_threadf()
    test_metaclase()
    test_decorador()
    test_modulo()
    test_ejemplo_practico()
    comparacion_metodos()