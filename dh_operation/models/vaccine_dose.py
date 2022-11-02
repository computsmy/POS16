from odoo import models, fields, api,_
from odoo.exceptions import *
class VaccinationDose(models.Model):
    _name = "vaccination.dose"
    _description = "List of Vaccination Dose"

    name = fields.Char(string='Vaccine Dose',required=1)
    active = fields.Boolean('Active')