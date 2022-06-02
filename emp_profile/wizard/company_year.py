from odoo import models, fields, api, _


class hr_company(models.Model):
    _name = 'wizard.company'
    _description = 'wizard.company'
    _rec_name = "ofcmp"

    ofcmp = fields.Integer(string="Total Experince")

    def action_done(self):
        return