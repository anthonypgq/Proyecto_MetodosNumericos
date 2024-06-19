# Proyecto_MetodosNumericos

# Calculadora de Ahorros

Esta es una aplicación de calculadora de ahorros que permite calcular la tasa de interés necesaria para alcanzar un valor final deseado, dado un depósito inicial, aportes periódicos y un período de tiempo específico.

## Instalación

### Instalar Dependencias

Asegúrate de tener instalado Python en tu sistema. Este script es compatible con Python 3.x. Puedes descargar e instalar Python desde [python.org](https://www.python.org/downloads/).

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

## Uso

1. **Ejecutar el Script**

    Ejecuta el archivo `Proyecto_Ahorro.py` para iniciar la aplicación de la calculadora de ahorros.

    ```bash
    python Proyecto_Ahorro.py
    ```

2. **Interfaz de Usuario**

    - **Depósito Inicial ($)**: Introduce el monto inicial del depósito. Debe ser al menos 50.
    - **Aportes ($)**: Introduce el monto de los aportes periódicos. Debe ser al menos 5.
    - **Valor Final Deseado ($)**: Introduce el valor final que deseas alcanzar.
    - **Periodos (años)**: Introduce el número de años durante los cuales se realizarán los aportes.
    - **Frecuencia de Aportes**: Selecciona la frecuencia de los aportes (semanal, mensual, bimestral, trimestral).

3. **Calcular la Tasa de Interés**

    Haz clic en el botón "Calcular Tasa de Interés". Si los datos son válidos, se mostrará la tasa de interés necesaria para alcanzar el valor final deseado. También se mostrará un gráfico de la evolución del saldo de ahorros a lo largo del tiempo.

4. **Errores Comunes**

    - Si el depósito inicial es menor de 50 o los aportes son menores de 5, se mostrará un mensaje de error.
    - Si no es posible alcanzar el valor final con las condiciones dadas, se mostrará un mensaje de error.

## Ejemplo de Uso

1. **Depósito Inicial ($)**: `100`
2. **Aportes ($)**: `10`
3. **Valor Final Deseado ($)**: `5000`
4. **Periodos (años)**: `10`
5. **Frecuencia de Aportes**: `Mensual`

Haz clic en "Calcular Tasa de Interés". Si los datos son válidos, se calculará la tasa de interés y se mostrará un gráfico de la evolución del saldo.

## Notas Adicionales

- Asegúrate de que todos los campos estén llenos y que los valores sean numéricos antes de hacer clic en "Calcular Tasa de Interés".
- La tasa de interés se muestra en porcentaje.
- Si necesitas ajustar el tamaño de la ventana de la aplicación, puedes hacerlo manualmente.

¡Y eso es todo! Ahora tienes una guía completa para instalar y usar tu calculadora de ahorros.
