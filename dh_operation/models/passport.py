from odoo import fields,models,api,_

class Passport(models.Model):
    _name = 'passport'
    _description = 'Model to add passport information'

    name = fields.Char('Name')
    passport_number = fields.Char('Passport Number')
    passport_issue_date = fields.Date('Passport Issue Date')
    passport_expiry_date = fields.Date('Passport Expiry Date')
    passport_applying_date = fields.Date('Passport Applying Date')
    passport_releasing_date = fields.Date('Passport Releasing Date')
    applicant_id = fields.Many2one('applicant',string="Applicant")
    passport_location = fields.Selection([
        ('agency','Agency'),
        ('agent','Agent'),
        ('applicant','Applicant')
    ])
    company_id = fields.Many2one('res.company')