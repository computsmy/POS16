from odoo import fields,models,api,_

class VisaSticker(models.Model):
    _name = 'visa.sticker'
    _description = 'Workers Visa Sticker Records'

    name = fields.Char('Name')
    enjaz_encoded = fields.Boolean('Enjaz Encoded')
    visa_filing_date = fields.Date('Visa Filing Date')
    visa_stamp_date = fields.Date('Visa Stamp Date')
    visa_expiry_date = fields.Date('Visa Expiry Date')
    applicant_id = fields.Many2one('applicant')
    visa_release_date = fields.Date('Visa Release Date')
    visa_number = fields.Char('Visa Number')
    company_id = fields.Many2one('res.company')