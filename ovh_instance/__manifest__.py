# © 2024 Halltic Tech - Tristán Mozos Pérez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'OVH Instance Manager',
    'version': '1.0',
    'author': 'Tu Nombre',
    'category': 'Tools',
    'description': 'Módulo para gestionar instancias de OVH',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/ovh_instance_view.xml',
        'views/ovh_instance_views.xml',
        'views/ovh_instance_menu.xml',
    ],
    'installable': True,
}

