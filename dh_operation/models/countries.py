from odoo import fields,models,api,_

class Countries(models.Model):
    _name = 'dh.countries'
    _description = 'Countries used for DH Operation only'

    name = fields.Char('Country Name')
    active = fields.Boolean('Active')
