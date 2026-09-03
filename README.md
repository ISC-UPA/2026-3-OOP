 Hola Estudiantes de Tercero
 Bienvenidos a POO
 ---

```mermaid
flowchart TD
A[Inicio] --> B{¿Está logueado?}
B -->|Sí| C[Página Principal]
B -->|No| D[Pantalla de Login]
D --> E[Verificar Credenciales]
E -->|Correctas| C
E -->|Incorrectas| D
C --> F[Fin]
```

> [!CAUTION]
> POO
>
