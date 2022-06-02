# -*- coding: utf-8 -*-
# from odoo import http


# class EmpProfile(http.Controller):
#     @http.route('/emp_profile/emp_profile', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/emp_profile/emp_profile/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('emp_profile.listing', {
#             'root': '/emp_profile/emp_profile',
#             'objects': http.request.env['emp_profile.emp_profile'].search([]),
#         })

#     @http.route('/emp_profile/emp_profile/objects/<model("emp_profile.emp_profile"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('emp_profile.object', {
#             'object': obj
#         })
