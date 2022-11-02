from odoo import fields,models,api,_

class ApplicantLocation(models.Model):
    _name = "applicant.location"
    _description = "Location of the applicant is located"

    name = fields.Char(string="Location")
    active = fields.Boolean('Active')
    company_id = fields.Many2one('res.company')