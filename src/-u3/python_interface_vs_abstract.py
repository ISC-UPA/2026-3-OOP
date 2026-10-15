import os, sys
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

# ============================================
# 1. ABC COMO "INTERFACE" (solo métodos abstractos)
# ============================================
class ITransporte(ABC):
    """
    Simula una Interface: solo métodos abstractos, sin implementación
    """
    
    @abstractmethod
    def entregar(self) -> None:
        pass
    
    @abstractmethod
    def obtener_capacidad(self) -> int:
        pass
    
    @abstractmethod
    def obtener_costo(self) -> float:
        pass

# Implementación concreta
class Camion(ITransporte):
    def entregar(self) -> None:
        print("🚚 Entregando por tierra")
    
    def obtener_capacidad(self) -> int:
        return 1000
    
    def obtener_costo(self) -> float:
        return 50.0

# ============================================
# 2. CLASE ABSTRACTA VERDADERA (con estado y lógica)
# ============================================
class LogisticaBase(ABC):
    """
    Clase Abstracta: tiene atributos, métodos concretos Y abstractos
    """
    
    def __init__(self, empresa: str):
        self.empresa = empresa  # ← Atributo de instancia
        self.entregas_realizadas = 0
        self.costo_total = 0.0
    
    @abstractmethod
    def crear_transporte(self) -> ITransporte:
        """Método abstracto - debe implementarse en subclases"""
        pass
    
    # Métodos concretos con lógica compartida
    def planificar_entrega(self) -> None:
        """Método concreto - ya tiene implementación"""
        transporte = self.crear_transporte()
        
        print(f"\n=== {self.empresa} ===")
        print(f"Entregas previas: {self.entregas_realizadas}")
        transporte.entregar()
        
        # Lógica compartida por todas las subclases
        self.entregas_realizadas += 1
        self.costo_total += transporte.obtener_costo()
        
        print(f"Costo: ${transporte.obtener_costo()}")
        print(f"Total acumulado: ${self.costo_total}")
    
    def generar_reporte(self) -> str:
        """Otro método concreto"""
        return f"{self.empresa}: {self.entregas_realizadas} entregas, ${self.costo_total} total"

# Subclases concretas
class LogisticaTerrestre(LogisticaBase):
    def crear_transporte(self) -> ITransporte:
        return Camion()

class Barco(ITransporte):
    def entregar(self) -> None:
        print("🚢 Entregando por mar")
    
    def obtener_capacidad(self) -> int:
        return 10000
    
    def obtener_costo(self) -> float:
        return 200.0

class LogisticaMaritima(LogisticaBase):
    def crear_transporte(self) -> ITransporte:
        return Barco()

# ============================================
# 3. PROTOCOL (enfoque pythonic moderno)
# ============================================
@runtime_checkable
class TransporteProtocol(Protocol):
    """
    Protocol: define la "forma" sin requerir herencia explícita
    Usa structural subtyping (duck typing estático)
    """
    
    def entregar(self) -> None: ...
    def obtener_capacidad(self) -> int: ...
    def obtener_costo(self) -> float: ...

# Esta clase NO hereda de TransporteProtocol pero cumple el protocolo
class Avion:  # ← No hereda de nada
    def entregar(self) -> None:
        print("✈️ Entregando por aire")
    
    def obtener_capacidad(self) -> int:
        return 5000
    
    def obtener_costo(self) -> float:
        return 500.0

# Función que acepta cualquier cosa que cumpla el Protocol
def procesar_transporte(transporte: TransporteProtocol) -> None:
    """
    Acepta cualquier objeto que tenga los métodos requeridos,
    sin importar si hereda explícitamente o no
    """
    print(f"Capacidad: {transporte.obtener_capacidad()} kg")
    transporte.entregar()
    print(f"Costo: ${transporte.obtener_costo()}")

# ============================================
# 4. DEMOSTRACIÓN DE DIFERENCIAS
# ============================================

def ejemplo_interface_vs_abstracta():
    print("=" * 60)
    print("DIFERENCIA 1: ABC como Interface vs Clase Abstracta")
    print("=" * 60)
    
    # LogisticaBase tiene estado y comportamiento compartido
    logistica1 = LogisticaTerrestre("Transportes Rápidos SA")
    logistica1.planificar_entrega()
    print(f"\nReporte: {logistica1.generar_reporte()}")
    
    logistica2 = LogisticaMaritima("NaviCarga Internacional")
    logistica2.planificar_entrega()
    print(f"\nReporte: {logistica2.generar_reporte()}")

def ejemplo_protocol():
    print("\n" + "=" * 60)
    print("DIFERENCIA 2: Protocol (sin herencia explícita)")
    print("=" * 60)
    
    # Avion NO hereda de ninguna clase base, pero funciona
    avion = Avion()
    print("\n🔍 Avion NO hereda de TransporteProtocol:")
    print(f'¿Es instancia de TransporteProtocol? {isinstance(avion, TransporteProtocol)}')
    print("Pero aún así funciona con la función tipada:")
    procesar_transporte(avion)
    
    # También funciona con clases que SÍ heredan
    print("\n🔍 Camion SÍ hereda de ITransporte:")
    camion = Camion()
    procesar_transporte(camion)

def ejemplo_errores():
    print("\n" + "=" * 60)
    print("DIFERENCIA 3: Errores en tiempo de ejecución")
    print("=" * 60)
    
    # Esto genera error: no puedes instanciar una clase abstracta
    print("\n❌ Intentando instanciar clase abstracta:")
    try:
        # logistica = LogisticaBase("Test")  # Descomenta para ver el error
        print("No se puede instanciar LogisticaBase directamente")
    except TypeError as e:
        print(f"Error: {e}")
    
    # Esto también genera error: falta implementar método abstracto
    print("\n❌ Subclase sin implementar método abstracto:")
    try:
        class LogisticaIncompleta(LogisticaBase):
            pass  # ¡Falta implementar crear_transporte()!
        
        # logistica = LogisticaIncompleta("Test")  # Descomenta para error
        print("LogisticaIncompleta no implementa crear_transporte()")
    except TypeError as e:
        print(f"Error: {e}")

# ============================================
# COMPARACIÓN VISUAL
# ============================================
def comparacion_visual():
    print("\n" + "=" * 60)
    print("RESUMEN: ¿Cuándo usar cada uno?")
    print("=" * 60)
    
    print("""
    📋 ABC como "INTERFACE" (solo @abstractmethod):
       ✓ Cuando quieres definir un contrato puro
       ✓ Sin estado ni lógica compartida
       ✓ Ejemplo: IRepositorio, IServicio, IValidador
    
    🏗️  CLASE ABSTRACTA (ABC con estado y métodos concretos):
       ✓ Cuando hay lógica compartida entre subclases
       ✓ Necesitas mantener estado común
       ✓ Template Method pattern
       ✓ Ejemplo: LogisticaBase, AnimalBase, VehiculoBase
    
    🦆 PROTOCOL (duck typing estático):
       ✓ Más pythonic y flexible
       ✓ No requiere herencia explícita
       ✓ Mejor para type checking con mypy
       ✓ Ejemplo: Comparable, Iterable, Callable
    """)

# ============================================
# BONUS: Herencia múltiple en Python
# ============================================
class IAlmacenable(ABC):
    @abstractmethod
    def guardar(self) -> None:
        pass

class ISerializable(ABC):
    @abstractmethod
    def to_json(self) -> str:
        pass

# Python permite herencia múltiple de interfaces
class Documento(IAlmacenable, ISerializable):
    def guardar(self) -> None:
        print("💾 Guardando documento")
    
    def to_json(self) -> str:
        return '{"tipo": "documento"}'

def ejemplo_herencia_multiple():
    print("\n" + "=" * 60)
    print("BONUS: Herencia múltiple (como en Java con interfaces)")
    print("=" * 60)
    
    doc = Documento()
    doc.guardar()
    print(f"JSON: {doc.to_json()}")

# ============================================
# MAIN
# ============================================
if __name__ == "__main__":
    os.system("cls")
    ejemplo_interface_vs_abstracta()
    ejemplo_protocol()
    ejemplo_errores()
    comparacion_visual()
    ejemplo_herencia_multiple()