from odoo import models, fields, api,_
from odoo.exceptions import *

class WorkExperience(models.Model):
    _name = "work.experience"
    _description = "Lines to add work experience in Application Form"

    name = fields.Char(string='Position Name',required=1,stored=1,index=1)
    job_location = fields.Selection([
        ('local','Local'),
        ('overseas','Overseas')
    ])
    start_date = fields.Date(string="Job Start Date")
    end_date = fields.Date(string="Job End Date")
    description = fields.Text(string="Description")
    application_id = fields.Many2one('applicant')