from odoo import fields,models,api,_

class Skills(models.Model):
    _name = 'skills'
    _description = 'Skills for Workers'

    name = fields.Char('Skills')
    active = fields.Boolean('Active')