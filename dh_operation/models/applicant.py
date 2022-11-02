from odoo import models, fields, api,_
from odoo.exceptions import *

class DHOperation(models.Model):
    _name = "applicant"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Domestic Helper Operation Application"

    name = fields.Char('Name',required=1)
    image = fields.Binary('Image')
    state = fields.Selection([
        ('draft','Draft'),
        ('ready','Ready'),
        ('progress','In Progress'),
        ('booking','For Booking'),
        ('booked','Booked'),
        ('deployed','Deployed')
    ])
    contact_number = fields.Char('Contact Number')
    id_number = fields.Char('ID Number')
    birth_date = fields.Char('Birth Date')
    age = fields.Integer('Age')
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')
    ])
    height = fields.Float('Height (CM)')
    weight = fields.Float('Weight (KG)')
    marital_status = fields.Selection([
        ('single','Single'),
        ('married','Married'),
        ('divorced','Divorced'),
        ('dwk','Divorced With Kids'),
    ])
    num_of_child = fields.Integer('Number Of Children')
    full_address = fields.Text('Full Address')
    process_remarks = fields.Text('Process Remarks')
    jobs_id = fields.Many2one('dh.jobs')
    country_id = fields.Many2one('dh.countries')
    location = fields.Many2one('applicant.location')
    agent_id = fields.Many2one('res.partner')
    fra = fields.Many2one('res.partner',string="FRA")
    cv_sent_date = fields.Date('CV Sent Date')
    emergency_name = fields.Char('Emergency Contact Name')
    emergency_num = fields.Char('Emergency Contact Number')
    video_interviewer = fields.Many2one('res.partner',string="Video Interviewer")
    school_interviewer = fields.Many2one('res.partner',string="School Interviewer")
    vid_interview_date = fields.Date('Video Interviewer Date')
    school_interview_date = fields.Date('School Interviewer Date')
    education = fields.Selection([
        ('primary','Primary'),
        ('secondary','Secondary'),
        ('craft','Craft Certificate'),
        ('diploma','Diploma'),
        ('higher_diploma','Higher Diploma'),
        ('certificate','Certificate'),
        ('university','University'),
    ])
    english_level = fields.Selection([
        ('none','No English'),
        ('partial','Cant Speak but Can Understand'),
        ('full','Can Speak and Can Understand'),
    ])
    previous_experience = fields.Many2many('skills','previous_skill_rel')
    willing_to = fields.Many2many('skills','willing_to_rel')

    abroad_exp = fields.Selection([
        ('yes','Yes'),
        ('no','No')
    ])
    arabic_level = fields.Selection([
        ('none','None'),
        ('partial','Cant Speak but Can Understand'),
        ('full','Can Speak and Can Understand'),
    ])

    passport_status = fields.Selection([
        ('none','No Passport'),
        ('applying','For Applying'),
        ('releasing','For Releasing'),
        ('valid','Valid'),
        ('24month','Expire in 24 Month'),
        ('18month','Expire in 18 Month'),
        ('expired','Expired')
    ])

    full_medical = fields.Selection([
        ('incomplete','Incomplete Requirement'),
        ('ready','Ready to Process'),
        ('process','In Process'),
        ('fit','Fit to Work'),
        ('unfit','Unfit')
    ])

    contract_status = fields.Selection([
        ('waiting_selection','Waiting Selection'),
        ('waiting_signature','Waiting Signature'),
        ('eemis_approval','For EEMIS Approval'),
        ('process','In Process'),
        ('waiting','Waiting New Contract'),
        ('deployed','Deployed'),
    ])

    musand_status = fields.Selection([
        ('encoding','For Encoding'),
        ('encoded','Encoded'),
        ('exist','Already Exist'),
        ('epro_approved','EPRO Approved'),
        ('fmol_approval','For FMOL Approval'),
        ('fmol_approved','FMOL Approved'),
        ('cancellation','Cancellation')
    ])

    school_certificate = fields.Selection([
        ('incomplete','Incomplete Requirement'),
        ('ready','Ready to Process'),
        ('process','In Process'),
        ('30days','Expire in 30 Days'),
        ('15days','Expire in 15 Days'),
        ('expired','Expired')
    ])

    good_conduct = fields.Selection([
        ('incomplete', 'Incomplete Requirement'),
        ('ready', 'Ready to Process'),
        ('process', 'In Process'),
        ('30days', 'Expire in 30 Days'),
        ('15days', 'Expire in 15 Days'),
        ('expired', 'Expired')
    ])

    visa_sticker = fields.Selection([
        ('incomplete', 'Incomplete Requirement'),
        ('ready', 'Ready to Process'),
        ('enjaz_encoded','Enjaz Encoded'),
        ('process', 'In Process'),
        ('30days', 'Expire in 30 Days'),
        ('15days', 'Expire in 15 Days'),
        ('expired', 'Expired')
    ])

    airport_clearance = fields.Selection([
        ('incomplete', 'Incomplete Requirement'),
        ('ready', 'Ready to Process'),
        ('process', 'In Process'),
        ('30days', 'Expire in 30 Days'),
        ('15days', 'Expire in 15 Days'),
        ('expired', 'Expired')
    ])

    office_arrival_date = fields.Date('Office Arrival Date')

    international_flight = fields.Selection([
        ('incomplete','Incomplete Requirement'),
        ('ready','Ready for Booking'),
        ('waiting','Waiting For Flight'),
        ('deployed','Deployed')
    ])

    _2x2_pic = fields.Binary('2 x 2 Pic')
    full_body_pic = fields.Binary('Full Body Pic')
    work_experience = fields.One2many('work.experience','application_id')
    vaccine = fields.One2many('vaccination','application_id')
    company_id = fields.Many2one('res.company')

    contract_count = fields.Integer(string="Contract Count", compute="_compute_contract_count")
    def _compute_contract_count(self):
        for record in self:
            contract_count = self.env['dh.contract'].search_count([('applicant_id','=',record.id)])
            record.contract_count = contract_count
    def action_contract(self):
        return{
            'type' : 'ir.actions.act_window',
            'name' : 'Contracts',
            'res_model' : 'dh.contract',
            'domain': [('applicant_id','=',self.id)],
            'view_mode' : 'tree,form',
            'target' : 'current'
        }

    passport_count = fields.Integer(string="Passport Count", compute="_compute_passport_count")
    def _compute_passport_count(self):
        for record in self:
            passport_count = self.env['passport'].search_count([('applicant_id','=',record.id)])
            record.passport_count = passport_count
    def action_passport(self):
        return{
            'type' : 'ir.actions.act_window',
            'name' : 'Passport',
            'res_model' : 'passport',
            'domain': [('applicant_id','=',self.id)],
            'view_mode' : 'tree,form',
            'target' : 'current'
        }

    medical_record_count = fields.Integer(string="Medical Record Count", compute="_compute_medical_record_count")
    def _compute_medical_record_count(self):
        for record in self:
            medical_record_count = self.env['passport'].search_count([('applicant_id','=',record.id)])
            record.medical_record_count = medical_record_count
    def action_medical_record(self):
        return{
            'type' : 'ir.actions.act_window',
            'name' : 'Medical Record',
            'res_model' : 'medical.record',
            'domain': [('applicant_id','=',self.id)],
            'view_mode' : 'tree,form',
            'target' : 'current'
        }

    school_training_count = fields.Integer(string="School Training Count", compute="_compute_school_training_count")
    def _compute_school_training_count(self):
        for record in self:
            school_training_count = self.env['passport'].search_count([('applicant_id','=',record.id)])
            record.school_training_count = school_training_count
    def action_school_training(self):
        return{
            'type' : 'ir.actions.act_window',
            'name' : 'School Training',
            'res_model' : 'school.training',
            'domain': [('applicant_id','=',self.id)],
            'view_mode' : 'tree,form',
            'target' : 'current'
        }

    visa_sticker_count = fields.Integer(string="Visa Sticker Count", compute="_compute_visa_sticker_count")
    def _compute_visa_sticker_count(self):
        for record in self:
            visa_sticker_count = self.env['visa.sticker'].search_count([('applicant_id','=',record.id)])
            record.visa_sticker_count = visa_sticker_count
    def action_visa_sticker(self):
        return{
            'type' : 'ir.actions.act_window',
            'name' : 'Visa Sticker',
            'res_model' : 'visa.sticker',
            'domain': [('applicant_id','=',self.id)],
            'view_mode' : 'tree,form',
            'target' : 'current'
        }

    airport_clearance_count = fields.Integer(string="Airport Clearance", compute="_compute_airport_clearance_count")
    def _compute_airport_clearance_count(self):
        for record in self:
            airport_clearance_count = self.env['airport.clearance'].search_count([('applicant_id','=',record.id)])
            record.airport_clearance_count = airport_clearance_count
    def action_airport_clearance(self):
        return{
            'type' : 'ir.actions.act_window',
            'name' : 'Airport Clearance',
            'res_model' : 'airport.clearance',
            'domain': [('applicant_id','=',self.id)],
            'view_mode' : 'tree,form',
            'target' : 'current'
        }