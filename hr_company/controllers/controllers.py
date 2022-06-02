# -*- coding: utf-8 -*-
# from odoo import http


# class HrCompany(http.Controller):
#     @http.route('/hr_company/hr_company', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_company/hr_company/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_company.listing', {
#             'root': '/hr_company/hr_company',
#             'objects': http.request.env['hr_company.hr_company'].search([]),
#         })

#     @http.route('/hr_company/hr_company/objects/<model("hr_company.hr_company"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_company.object', {
#             'object': obj
#         })
