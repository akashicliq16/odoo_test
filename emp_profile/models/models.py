# -*- coding: utf-8 -*-
# import string
from unittest import result
from odoo import models, fields, api, _
import datetime
from odoo.exceptions import ValidationError
# import re

class Address(models.Model):
    _name = "address"
    _rec_name = "street"

    street = fields.Char("Street")
    street_one = fields.Char("Street2")
    city = fields.Char("City")
    state = fields.Char("State")
    country = fields.Char("Country")
    zip_code = fields.Char("Zip Code")

class emp_profile(models.Model):
    _name = 'emp_profile.emp_profile'
    _inherit = "address"
    _description = 'emp_profile.emp_profile'
    _rec_name  ="name"
    _order = "sequence"
    
    sequence = fields.Integer("employee sequence")
    name = fields.Char(string="Full Name", help="This field is requird employee full name!", required=True, size=25, index=True)
    comp_id = fields.Many2one("hr_company.hr_company", string="Company",
    # Domain Defination:- Odoo domain is used to select records from a model or database table. It is a very common use case when you need to display a subset 
    # of all available records from an action, or to allow only a subset of possible records to be the target of a many2one relation.
                            # domain = "[('currency_id','=','INR'),('status','=','True')]" 

                            # Dynamic Field.
                            # domain = "[('currency_id','=','INR')]"
                                )
    email = fields.Char(string="email", help="This employee email id fields.",size=80)
    phone = fields.Char(string="Phone Number", help="This employee phone number fields.")
    cv = fields.Binary(string="CV Upload", help="This is a CV Upload Fields")
    bday = fields.Date(string="Birthday",help="This is Birthaday fields")
    age = fields.Char(string=" Age", help="This is a Age Fields.", compute="_get_age_employee") # compute field
    currency_id = fields.Many2one("res.currency", string="currency_id", help="This field using currency type")
    total_selary = fields.Float(string="Total selary")
    employeestatus = fields.Boolean(string="Active", help="This is status fields.")
    departments = fields.Many2one('department.types', string="Department",help="This fields is a Department types")
    gender = fields.Selection([("male","Male"),("female","Female")])
    name_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))

    # Sequence helping code.
    @api.model
    def create(self,vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('emp_profile.emp_profile') or _('New')
        result = super(emp_profile, self).create(vals)
        return result
    
        
    
    _sql_constraints = [
        # ('unique_name','unique (name)','name must be unique.'),
        # ('unique_name','unique (age >=18)','Minimum 18 year age required. '),
        ('unique_phone','unique (phone)', 'Phone Number Must Be Unique')
    ]

    # ORM Method.
    def action_confirm(self):
        for rec in self:
            # Odoo Search ORM.
            name = self.env['emp_profile.emp_profile'].search([])
            # print("employee...",name)
            male_employee = self.env['emp_profile.emp_profile'].search([('gender','=','male')])
            # print('male employee...', male_employee)
            female_employee = self.env['emp_profile.emp_profile'].search([('gender','=','female')])
            # print('male employee...', female_employee)

            # Odoo Search Count.
            employee_count = self.env['emp_profile.emp_profile'].search_count([])
            # print("number of the employee...",employee_count)

            male_employee_count = self.env['emp_profile.emp_profile'].search_count(['|', ('gender','=','male'),('age','>=','18')])
            # print('male employee...', male_employee_count)

            # Odoo Browse ORM.
            browse_result = self.env['emp_profile.emp_profile'].browse(500)
            # print("browe.... ", browse_result)

            # Odoo Existing ORM.
            # if browse_result.exists():
            #     print("Existing")
            # else:
            #     print("Noooooooooooooooooooooooooo")

            # Odoo create ORM.
        vals ={
            'name': 'Odoo Employee',
            'email' :'exampul@gmail.com'    
        } 
        self.env['emp_profile.emp_profile'].create(vals)

        # Odoo Write ORM.
        record_to_update = self.env['emp_profile.emp_profile'].browse(10)
        if record_to_update.exists():
            vals={
                'email': 'noexampal@gmail.com'
            }
            record_to_update.write(vals)

        # Odoo Copy ORM.
        # record_to_copy = self.env['emp_profile.emp_profile'].browse(5)
        # record_to_copy.copy()

        # Odoo unlink ORM.
        record_to_copy = self.env['emp_profile.emp_profile'].browse(5)
        record_to_copy.unlink()  

    def action_wizard(self):
        return{
            "type": 'ir.actions.act_window',
            "res_model": 'wizard.company',
            "view_mode": 'form',
            "target": 'new',
        }
        
    def action_emp(self):
        # print("Test!!!!!!!!!!!!!!!!!!!!!!!")
        return {
          "type": 'ir.actions.act_window',
          "name": 'Company',
          "res_model": 'hr_company.hr_company',
          "domain" : [('comp_id','=',self.id)],
          "view_mode": 'tree,form',
          "target": 'new',
        }

    # whatsapp_share message code.
    def whatsapp_share(self):
        if not self.comp_id.phone:
            raise ValidationError(_("Missing Phone Number in Patient record"))
        message= 'Hi %s , your cv share: %s' % (self.comp_id.currency_id,self.comp_id.state)
        whatsapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.comp_id.phone, message)
        return{
            'type':'ir.actions.act_url',
            'target' : 'new',
            'url' : whatsapp_api_url
        }
    
    @api.depends("bday") # depends using on time change output
    def _get_age_employee(self):       # compute show output change save button to show output.
        today_date = datetime.date.today()
        for em in self:
            if em.bday:
                embday = fields.Datetime.to_datetime(em.bday).date()
                total_age = str(int((today_date-embday).days/365))
                em.age = total_age
            else:
                em.age = "Not Provide......"


