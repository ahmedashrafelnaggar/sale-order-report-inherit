# import json
# from odoo import http
# from odoo.http import request
#
#
# class PatientApi(http.Controller):
#     # methods = ["POST"] when you do creation u should use method post
#     @http.route("/api/patient", methods=["POST"], type="http", auth="none", csrf=False)
#     def post_patient(self):
#         # wrote the data in post man , now want to get this data  from postman to do creation
#         args = request.httprequest.data.decode()
#         print(args)
#         # this mean I say after you get the data make this data json in variable vals
#         vals = json.loads(args)
#         # # u will create the data now, we use now sudo because we put auth=none
#         res = request.env['hospital.patient'].sudo().create(vals)
#         print(res)