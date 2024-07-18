# © 2024 Halltic Tech - Tristán Mozos Pérez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api
import ovh

class OvhInstance(models.Model):
    _name = 'ovh.instance'
    _description = 'OVH Instance'

    name = fields.Char('Instance Name', required=True)
    client_id = fields.Many2one('res.partner', string='Client', required=True)
    state = fields.Selection([
        ('new', 'Nueva'),
        ('creating', 'En creación'),
        ('running', 'Funcionando'),
        ('stopped', 'Parada'),
        ('deleted', 'Eliminada'),
    ], string='State', default='new')
    trial_period = fields.Integer('Trial Period (days)', default=15)
    expiration_date = fields.Date('Expiration Date')

    @api.model
    def create_instance(self):
        client = ovh.Client(
            endpoint='ovh-eu',
            application_key='your_app_key',
            application_secret='your_app_secret',
            consumer_key='your_consumer_key',
        )
        # Implementar la lógica para crear una instancia en OVH y configurar Odoo
        self.state = 'creating'

    def start_instance(self):
        # Lógica para arrancar la instancia en OVH
        self.state = 'running'

    def stop_instance(self):
        # Lógica para detener la instancia en OVH
        self.state = 'stopped'

    def delete_instance(self):
        # Lógica para eliminar la instancia en OVH
        self.state = 'deleted'
