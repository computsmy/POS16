from odoo import models, fields, api,_
from odoo.exceptions import *

class VaccinationBrand(models.Model):
    _name = "vaccination.brand"
    _description = "List of Vaccination Brand"

    name = fields.Char(string='Vaccination Brand Name',required=1)
    active = fields.Boolean('Active')