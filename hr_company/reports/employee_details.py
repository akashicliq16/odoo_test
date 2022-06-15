from odoo import api, models, _

class EmployeeDetailReport(models.AbstractModel):
    _name = 'report.hr_company.report_companys'
# from pyexpat import model
from odoo import api,fields,models, _

class EmployeeDetailReport(models.Model):
    _name = 'hr_company.hr_company.report_companys'
    _description = 'Employee Details Report'

    @api.model
    def _get_report_values(self,docids, data=None):
        print("Yes Entered here in the function")
        print("docids",docids)
        docs = self.env['hr_company.hr_company'].browse(docids[0])
        hrlist=[]
        for li in docs:
            vals = {
                'name':li.name,
                "phone":li.phone,
                'city':li.city
            }
            hrlist.append(vals)
            print("list....",hrlist)
        return {
            'doc_model' : 'hr_company.hr_company',
            'data' : data,
            'docs' : docs,
            'hrlist':hrlist,
            
        }