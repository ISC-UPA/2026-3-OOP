from abc import ABC, abstractmethod

# ============================================
# INTERFAZ PRODUCTO (Product)
# ============================================
class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass
    
    @abstractmethod
    def obtener_capacidad(self):
        pass

# ============================================
# PRODUCTOS CONCRETOS (Concrete Products)
# ============================================
class Camion(Transporte):
    def entregar(self):
        print("🚚 Entrega por TIERRA en camión")
    
    def obtener_capacidad(self):
        return 1000  # kg

class Barco(Transporte):
    def entregar(self):
        print("🚢 Entrega por MAR en barco")
    
    def obtener_capacidad(self):
        return 10000  # kg

class Avion(Transporte):
    def entregar(self):
        print("✈️ Entrega por AIRE en avión")
    
    def obtener_capacidad(self):
        return 5000  # kg

# ============================================
# CREADOR ABSTRACTO (Creator)
# ============================================
class Logistica(ABC):
    
    @abstractmethod
    def crear_transporte(self) -> Transporte:
        """Factory Method - debe ser implementado por subclases"""
        pass
    
    def planificar_entrega(self):
        """Método que usa el Factory Method"""
        # Llamamos al factory method para crear el transporte
        transporte = self.crear_transporte()
        
        print("Planificando entrega...")
        print(f"Capacidad: {transporte.obtener_capacidad()} kg")
        transporte.entregar()
        print("Entrega completada\n")

# ============================================
# CREADORES CONCRETOS (Concrete Creators)
# ============================================
class LogisticaTerrestre(Logistica):
    def crear_transporte(self) -> Transporte:
        return Camion()

class LogisticaMaritima(Logistica):
    def crear_transporte(self) -> Transporte:
        return Barco()

class LogisticaAerea(Logistica):
    def crear_transporte(self) -> Transporte:
        return Avion()

# ============================================
# EJEMPLO PRÁCTICO: Sistema de Notificaciones
# ============================================

# Interfaz Producto
class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str):
        pass

# Productos Concretos
class Email(Notificacion):
    def enviar(self, mensaje: str):
        print(f"📧 Enviando EMAIL: {mensaje}")

class SMS(Notificacion):
    def enviar(self, mensaje: str):
        print(f"📱 Enviando SMS: {mensaje}")

class PushNotification(Notificacion):
    def enviar(self, mensaje: str):
        print(f"🔔 Enviando PUSH: {mensaje}")

# Creador Abstracto
class NotificadorBase(ABC):
    
    @abstractmethod
    def crear_notificacion(self) -> Notificacion:
        pass
    
    def notificar(self, mensaje: str):
        notificacion = self.crear_notificacion()
        print("Preparando notificación...")
        notificacion.enviar(mensaje)

# Creadores Concretos
class NotificadorEmail(NotificadorBase):
    def crear_notificacion(self) -> Notificacion:
        return Email()

class NotificadorSMS(NotificadorBase):
    def crear_notificacion(self) -> Notificacion:
        return SMS()

class NotificadorPush(NotificadorBase):
    def crear_notificacion(self) -> Notificacion:
        return PushNotification()

# ============================================
# VERSIÓN PYTHONICA (usando funciones)
# ============================================
def crear_notificador_pythonic(tipo: str):
    """Factory function - enfoque más pythonic"""
    notificadores = {
        'email': Email,
        'sms': SMS,
        'push': PushNotification
    }
    
    clase_notificacion = notificadores.get(tipo.lower())
    if clase_notificacion:
        return clase_notificacion()
    else:
        raise ValueError(f"Tipo de notificación '{tipo}' no soportado")

# ============================================
# EJEMPLO CON TYPE HINTS Y DATACLASSES
# ============================================
from dataclasses import dataclass
from typing import Protocol

class TransporteProtocol(Protocol):
    """Protocol en lugar de ABC - más pythonic"""
    def entregar(self) -> None: ...
    def obtener_capacidad(self) -> int: ...

@dataclass
class Tren:
    """Usando dataclass para demostrar flexibilidad"""
    velocidad_max: int = 120
    
    def entregar(self):
        print(f"🚄 Entrega por TREN a {self.velocidad_max} km/h")
    
    def obtener_capacidad(self):
        return 8000

# ============================================
# MAIN - PRUEBAS
# ============================================
def main():
    print("=== EJEMPLO 1: SISTEMA DE LOGÍSTICA ===\n")
    
    # El cliente trabaja con la abstracción
    logisticas = [
        LogisticaTerrestre(),
        LogisticaMaritima(),
        LogisticaAerea()
    ]
    
    for logistica in logisticas:
        logistica.planificar_entrega()
    
    print("\n=== EJEMPLO 2: SISTEMA DE NOTIFICACIONES ===\n")
    
    mensaje = "¡Tienes un nuevo mensaje!"
    
    notificadores = [
        NotificadorEmail(),
        NotificadorSMS(),
        NotificadorPush()
    ]
    
    for notificador in notificadores:
        notificador.notificar(mensaje)
        print()
    
    print("\n=== EJEMPLO 3: VERSIÓN PYTHONICA (Factory Function) ===\n")
    
    # Enfoque más pythonic usando funciones
    tipos = ['email', 'sms', 'push']
    
    for tipo in tipos:
        notificacion = crear_notificador_pythonic(tipo)
        notificacion.enviar(f"Mensaje usando factory function - {tipo}")
    
    print("\n=== EJEMPLO 4: SELECCIÓN DINÁMICA ===\n")
    seleccionar_logistica_por_destino("internacional")
    seleccionar_logistica_por_destino("nacional")
    seleccionar_logistica_por_destino("local")
    
    print("\n=== EJEMPLO 5: USANDO DATACLASS Y PROTOCOL ===\n")
    tren = Tren(velocidad_max=200)
    print(f"Capacidad del tren: {tren.obtener_capacidad()} kg")
    tren.entregar()

def seleccionar_logistica_por_destino(destino: str):
    """Función que demuestra selección dinámica del factory"""
    
    factories = {
        'internacional': LogisticaAerea,
        'nacional': LogisticaTerrestre,
        'local': LogisticaMaritima
    }
    
    factory_class = factories.get(destino.lower(), LogisticaTerrestre)
    logistica = factory_class()
    
    print(f"Destino: {destino}")
    logistica.planificar_entrega()

# ============================================
# COMPARACIÓN: Decorator como Factory
# ============================================
def registrar_notificacion(nombre: str):
    """Decorator para auto-registro de notificaciones"""
    def decorator(cls):
        NotificadorRegistry.registrar(nombre, cls)
        return cls
    return decorator

class NotificadorRegistry:
    """Registry pattern combinado con Factory"""
    _notificadores = {}
    
    @classmethod
    def registrar(cls, nombre: str, notificador_class):
        cls._notificadores[nombre] = notificador_class
    
    @classmethod
    def crear(cls, nombre: str) -> Notificacion:
        notificador_class = cls._notificadores.get(nombre)
        if notificador_class:
            return notificador_class()
        raise ValueError(f"Notificador '{nombre}' no registrado")

# Uso del decorator
@registrar_notificacion('whatsapp')
class WhatsApp(Notificacion):
    def enviar(self, mensaje: str):
        print(f"💬 Enviando WHATSAPP: {mensaje}")

@registrar_notificacion('telegram')
class Telegram(Notificacion):
    def enviar(self, mensaje: str):
        print(f"✈️ Enviando TELEGRAM: {mensaje}")

def ejemplo_registry():
    print("\n=== EJEMPLO 6: REGISTRY PATTERN ===\n")
    
    # Las clases se auto-registran con el decorator
    whatsapp = NotificadorRegistry.crear('whatsapp')
    whatsapp.enviar("Mensaje por WhatsApp")
    
    telegram = NotificadorRegistry.crear('telegram')
    telegram.enviar("Mensaje por Telegram")

if __name__ == "__main__":
    main()
    ejemplo_registry()