# Objetivo

Se busca centralizar las pólizas que están próximas a vencer y las vencidas dentro de la ventana de 30 días, y en caso dado las polizas que ya pasaron esa ventans de renovación.

# Funcionalidades y Decisiones

- Listar pólizas
- Filtrar por estado
- Registrar gestión
- Renovar póliza

# No implementado

- Login
- Roles
- Notificaciones
- Integraciones externas
- Recuperación de contraseña 
- Auditoría avanzada 

Dado que e objetivo de la prueba es validar el flujo de gestión de renovaciones. La autenticación no aporta valor directo al problema de negocio dentro del tiempo disponible al igual que las notificaciones ya que eso implementaría integraciones externas, que no son deseadas en este caso.


# Modelo de datos (con supuestos)

Client [id, name, email, phone, document]
Policy [id, id_client, policy_number, _policy_type, description, issue_date, expiration_date, estatus, last_contact_date, renewed]
PolicyAction [id, id_policy, acction_date, notes]

Para simplificar el alcance, la aplicación inicia con datos precargados que representan la cartera de clientes de María. No se implementó la creación de clientes o pólizas desde la interfaz.

# Endpoints

GET /policies 
POST /policies/{id}/actions
POST /policies/{id}/renew

# Tests

- Ventana de 30 días
- Renovación
- Cálculo de días restantes

Test 1
Una póliza que vence en 10 días aparece en la lista.

Test 2
Una póliza vencida hace 20 días sigue apareciendo como renovable.

Test 3
Una póliza vencida hace 40 días aparece fuera de la ventana crítica.
