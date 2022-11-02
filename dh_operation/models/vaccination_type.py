from odoo import models, fields, api,_
from odoo.exceptions import *

class VaccinationType(models.Model):
    _name = "vaccination.type"
    _description = "List of Vaccination"

    name = fields.Char(string='Vaccination Name',required=1)
    active = fields.Boolean('Active')