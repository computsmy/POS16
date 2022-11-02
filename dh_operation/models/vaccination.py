from odoo import fields,models,api,_

class Vaccination(models.Model):
    _name = "vaccination"
    _description = "Lines to add vaccination in Application Form"

    name = fields.Char(string='name',compute="vaccine_name")
    vaccination_id = fields.Many2one('vaccination.type',string="Vaccination Type")
    vaccine_dose_id = fields.Many2one('vaccination.dose')
    date = fields.Date(string="Dose Date")
    vaccine_brand_id = fields.Many2one('vaccination.brand')
    application_id = fields.Many2one('applicant')
    @api.depends('name')
    def vaccine_name(self):
        for record in self:
            record['name'] = record.vaccination_id.name

