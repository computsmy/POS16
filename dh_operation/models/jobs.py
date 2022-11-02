from odoo import fields,models,api,_

class JobsType(models.Model):
    _name = 'dh.jobs'
    _description = 'Type of jobs the applicants are applying for'

    name = fields.Char('Job Title')
    active = fields.Boolean('Active')
    company_id = fields.Many2one('res.company')