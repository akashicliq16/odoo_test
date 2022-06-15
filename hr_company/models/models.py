# -*- coding: utf-8 -*-

# from asyncio import constants
# from email import message
# from email.policy import default
# import string
# from sys import maxsize
# from tracemalloc import DomainFilter
from tracemalloc import DomainFilter
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Address(models.Model):
    _name = "address"
    _rec_name = "street"

    street = fields.Char("Street")
    street_one = fields.Char("Street2")
    city = fields.Char("City")
    stat = fields.Char("State")
    country = fields.Char("Country")
    zip_code = fields.Char("Zip Code")

class hr_company(models.Model):
    _name = 'hr_company.hr_company'
    _description = 'hr_company.hr_company'
    _inherit = "address"
    _rec_name = "name"
    _order = "sequence"

    sequence = fields.Integer("company")
    name = fields.Char(string="Name Of Company", help="This is Name Of Company", required=True)
    
    emp_status = fields.Boolean(string="Active", help="This is status fields.")
    currency_id = fields.Many2one("res.currency", string="currency_id", help="This field using currency type")
    color = fields.Integer(string="Color")
    phone = fields.Char(string="Phone Number", help="This employee phone number fields.")
    state = fields.Selection([("draft","Draft"),("in_process","In Process"),("done","Done"),("cancel","Cancel")],default="draft",string="Status")
    company_seq = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    
    
    # eventcompute = fields.Integer(string="Event", compute="compute_event") # Add Compute Field.

    # Add Compute Field.
    # def compute_event(self):
    #     eventcompute = self.env['emp_profile.emp_profile'].search_count([('emp_id','=',self.id)])
    #     self.eventcompute = eventcompute

    @api.model
    def create(self,vals):
        if vals.get('company_seq', _('New')) == _('New'):
            vals['company_seq'] = self.env['ir.sequence'].next_by_code('hr_company.hr_company') or _('New')
        result = super(hr_company, self).create(vals)
        return result

    _sql_constraints = [
        ('unique_name','unique (name)','name must be unique.'),
        ('unique_phone','unique (phone)', 'Phone Number Must Be Unique')
    ]

    def print_report(self):
        return self.env.ref('hr_company.report_employee_payslip').report_action(self)

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

        
class Department(models.Model):
    _name="department.types"
    _order= "sequence"

    sequence = fields.Integer('sequence')
    name=fields.Char("Department")
   

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