# -*- coding: utf-8 -*-
{
    'name': "DH Operation",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.computs.com.my",
    'sequence': -999,
    'application': True,
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Domestic Helper',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menuitem.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/applicant.xml',
        'views/passport.xml',
        'views/medical_record.xml',
        'views/school_training.xml',
        'views/visa_sticker.xml',
        'views/airport_clearance.xml',
        'views/contract.xml',
        'views/countries.xml',
        'views/applicant_location.xml',
        'views/skills.xml',
        'views/jobs.xml',
        'views/vaccination_type.xml',
        'views/vaccination_dose.xml',
        'views/vaccination_brand.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
