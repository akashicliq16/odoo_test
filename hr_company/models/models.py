# -*- coding: utf-8 -*-

# from asyncio import constants
# from email import message
# from email.policy import default
# import string
# from sys import maxsize
# from tracemalloc import DomainFilter
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError



class hr_company(models.Model):
    _name = 'hr_company.hr_company'
    _description = 'hr_company.hr_company'
    _rec_name = "name"

    name = fields.Char(string="Name Of Company", help="This is Name Of Company", required=True)
    emp_id = fields.Many2one("emp_profile.emp_profile", string="Employee",
    # Domain Defination:- Odoo domain is used to select records from a model or database table. It is a very common use case when you need to display a subset 
    # of all available records from an action, or to allow only a subset of possible records to be the target of a many2one relation.
                            # domain = "[('currency_id','=','INR'),('status','=','True')]" 

                            # Dynamic Field.
                            # domain = "[('currency_id','=','INR')]"
                                )
    emp_status = fields.Boolean(string="Active", help="This is status fields.")
    currency_id = fields.Many2one("res.currency", string="currency_id", help="This field using currency type")
    color = fields.Integer(string="Color")
    phone = fields.Char(string="Phone Number", help="This employee phone number fields.",size=10)
    state = fields.Selection([("draft","Draft"),("in_process","In Process"),("done","Done"),("cancel","Cancel")],default="draft",string="Status")
    gender = fields.Selection([("male","Male"),("female","Female")], string="Gender", related='emp_id.gender') # related Field
    total_selary = fields.Float(string="Total selary")
    
    # eventcompute = fields.Integer(string="Event", compute="compute_event") # Add Compute Field.

    # Add Compute Field.
    # def compute_event(self):
    #     eventcompute = self.env['emp_profile.emp_profile'].search_count([('emp_id','=',self.id)])
    #     self.eventcompute = eventcompute


    _sql_constraints = [
        ('unique_name','unique (name)','name must be unique.'),
        ('unique_phone','unique (phone)', 'Phone Number Must Be Unique')
    ]

    def action_test(self):
        print("Button Click!!!!!!!!!!!!!!!1")

    # @api.constrains('phone')
    # def check_phone(self):
    #     for rec in self:
    #         patients = self.env['hr_company.hr_company'].search([('phone','=','rec.phone')]),('','!=','rec.id')
    #         if patients:
    #             raise ValidationError(_("Phone %s Already Exits" % rec.phone))

    @api.constrains('ofcmp')
    def year_ofcmp_name(self):
        for rec in self:
            if rec.ofcmp == 0:
                raise ValidationError(_("year of company Cannot Be Zero."))


    # The onchange mechanism in Odoo enables the feature to modify or update the value of a field if any update is done on the other fields.
    @api.onchange('emp_id')
    def onchange_emp_id(self):
        if self.emp_id:
            if self.emp_id.total_selary:
                self.total_selary = self.emp_id.total_selary
        else:
            self.total_selary = '0.00'

    # whatsapp_share message code.
    def whatsapp_share(self):
        if not self.emp_id.phone:
            raise ValidationError(_("Missing Phone Number in Patient record"))
        message= 'Hi %s , your cv share: %s' % (self.emp_id.name, self.emp_id.gender)
        whatsapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.emp_id.phone, message)
        return{
            'type':'ir.actions.act_url',
            'target' : 'new',
            'url' : whatsapp_api_url
        }

    def action_in_process(self):
        for rec in self:
            rec.state = 'in_process'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    # ORM Method.
    def action_confirm(self):
        for rec in self:
            # Odoo Search ORM.
            name = self.env['emp_profile.emp_profile'].search([])
            print("employee...",name)
            male_employee = self.env['emp_profile.emp_profile'].search([('gender','=','male')])
            print('male employee...', male_employee)
            female_employee = self.env['emp_profile.emp_profile'].search([('gender','=','female')])
            print('male employee...', female_employee)

        
    def action_emp(self):
        # print("Test!!!!!!!!!!!!!!!!!!!!!!!")
        return {
          "type": 'ir.actions.act_window',
          "name": 'Employee',
          "res_model": 'emp_profile.emp_profile',
          "domain" : [('emp_id','=',self.id)],
          "view_mode": 'tree,form',
          "target": 'current',
        }

class ResPartner(models.Model):
    _inherit = 'res.partner'

    company_type = fields.Selection(Selection_add=[('si','iCliQ Solution')])

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

# one2many
# class EmployeePo(models.Model):
#     _inherit = "emp_profile.emp_profile"

#     emp_list = fields.One2many("hr_company.hr_company","emp_id",string="employee_list") 