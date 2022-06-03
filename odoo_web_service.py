url = "http://localhost:8069"
db = "employee"
username = 'admin'
password = '1234'

import xmlrpc.client

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
print("details...",version)

uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
partner_id = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company','=',True]]], {'offset': 5, 'limit': 3})
print("partners... ",partner_id)

# Read records.
partners_rec = models.execute_kw(db, uid, password, 'res.partner', 'read', [partner_id], {'fields': ['id','name']})
print("partner_id.......")
for partner in partners_rec:
    print(partners_rec)

# Search and read.
abcd = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['id','name'], 'limit': 5})
print("abcd..........",abcd)

for pa in abcd:
    print(pa)

# Create records.
new_contect = models.execute_kw(db, uid, password, 'res.partner', 'create', [{'name': "Akash",'mobile':"123456789",'website':"www.test.com"}])
print("new_contect.......",new_contect)

# Update records
UPD_new = models.execute_kw(db, uid, password, 'res.partner', 'write', [[12], {'name': "akash",'mobile':"012346789",'website':"www.Your_Test.com"}])
print("UPD_new....", UPD_new)

delt_record = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['id', '=', 17]]])
print("delt_record....", delt_record)
