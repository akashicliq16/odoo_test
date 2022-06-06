import odoorpc

# Prepare the connection to the server
odoo = odoorpc.ODOO('localhost', port=8069)

# Check available databases
print(odoo.db.list())

# Login
odoo.login('employee', 'admin', '1234')

# Current user
user = odoo.env.user
print(user.name)            # name of the user connected
print(user.company_id.name) # the name of its company

if 'emp_profile.emp_profile' in odoo.env:
    emp_pro = odoo.env['emp_profile.emp_profile'].search([])
    print("Search.........",emp_pro)
    for lead in emp_pro:
        print("for.........",lead)
        emp_prof = odoo.env['emp_profile.emp_profile'].browse(emp_pro)
        print("emp_prof..........",emp_prof.name)
        # writing to the database.
        emp_prof.description = "odoo Akash"
        emp_prof.write({"email":'icliq@solution.com'})


# Use all methods of a model
# if 'emp_profile.emp_profile' in odoo.env:
#     emp_pro = odoo.env['emp_profile.emp_profile']
#     print("emp_pro.........",emp_pro)
#     emp_ids = emp_pro.search([])
#     print("emp_ids..........",emp_ids)
#     for emp in emp_pro.browse(emp_ids):
#         print(emp.name)
        # products = [line.product_id.name for line in emp.order_line]
        # print(products)