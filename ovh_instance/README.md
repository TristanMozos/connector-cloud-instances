# OVH Instance Manager for Odoo

## Descripción

El módulo **OVH Instance Manager** para Odoo permite gestionar instancias de OVH para que los clientes puedan probar una instancia de Odoo. También es útil para gestionar las instancias de los clientes que tienen contratado el alojamiento. Además, el módulo permite ver el estado de las instancias que estamos gestionando y gestionar el DNS para redireccionar el dominio hacia la dirección de la instancia.

## Funcionalidades

- Creación automática de instancias de Odoo para clientes.
- Gestión de VPS en OVH donde se instalan las instancias.
- Control de periodos de prueba (15 días, 1 mes, etc.) y eliminación de instancias al finalizar el periodo.
- Estados de las instancias: "Nueva", "En creación", "Funcionando", "Parada", y "Eliminada".
- Integración con la API de OVH para gestionar la creación, arranque, detención y eliminación de instancias.
- Gestión de DNS para redireccionar dominios a instancias específicas.

## Instalación

1. Clona este repositorio en la carpeta `addons` de tu instalación de Odoo.
   ```bash
   git clone https://github.com/tu-usuario/connector-ovh.git
