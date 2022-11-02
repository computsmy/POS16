from odoo import fields,models,api,_

class Contract(models.Model):
    _name = "dh.contract"
    _description = "Contract for workers"

    name = fields.Char('Name')
    contract_received_date = fields.Date('Contract Received Date')
    contract_signed_date = fields.Date('Contract Signed Date')
    applicant_id = fields.Many2one('applicant')
    company_id = fields.Many2one('res.company')
    employer_id = fields.Many2one('res.partner')
    id_number = fields.Char('ID Number')
    visa_number = fields.Char('Visa Number')
    employer_contact_number = fields.Char('Contact Number',related="employer_id.mobile")
    employer_email = fields.Char('Email Address',related="employer_id.email")