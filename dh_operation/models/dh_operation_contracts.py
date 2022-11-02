from odoo import fields,models,api,_

class DhOperationContracts(models.Model):
    _name = 'dh.operation.contract'
    _description = 'Contract for Dh Operation'

    name = fields.Char('name')
