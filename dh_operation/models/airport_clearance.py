from odoo import fields,models,api,_

class AirportClearance(models.Model):
    _name = "airport.clearance"
    _description = "Workers Airport Clearance datas"

    name = fields.Char('name')
    filling_date = fields.Date('Filling Date')
    applicant_id = fields.Many2one('applicant')
    approval_date = fields.Date('Approval Date')
    expiry_date = fields.Date('Expiry Date')
    company_id = fields.Many2one('res.company')


