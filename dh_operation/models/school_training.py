from odoo import fields,models,api,_

class SchoolTraining(models.Model):
    _name = 'school.training'
    _description = 'Workers School Training Records'

    name = fields.Char('Name')
    training_filing_date = fields.Date('Training Filing Date')
    start_date = fields.Date('Training Start Date')
    end_date = fields.Date('Training End Date')
    applicant_id = fields.Many2one('applicant')
    training_code = fields.Char('Training Batch Code')
    certificate_release_date = fields.Date('Certificate Release Date')
    certificate_number = fields.Char('Certificate Number')
    company_id = fields.Many2one('res.company')