from odoo import fields,models,api,_

class MedicalRecord(models.Model):
    _name = 'medical.record'
    _description = 'Medical Records of Workers'

    name = fields.Char('Name')
    medical_type = fields.Selection([
        ('small','Small Medical'),
        ('full','Full Medical')
    ])
    medical_date = fields.Date('Medical Date')
    medical_result = fields.Selection([
        ('progress','In Progress'),
        ('fit','Fit To Work'),
        ('unfit','Unfit To Work')
    ])
    unfit_reason = fields.Text('Unfit Reason')
    applicant_id = fields.Many2one('applicant')
    clinic_id = fields.Many2one('res.partner')
    medical_result_date = fields.Date('Medical Result Date')
    medical_expiry_date = fields.Date('Medical Expiry Date')
    medical_certificate_date = fields.Date('Medical Certificate Received Date')
    company_id = fields.Many2one('res.company')