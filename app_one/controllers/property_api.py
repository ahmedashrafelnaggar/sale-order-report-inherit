import json
from odoo import http
from odoo.http import request


class PropertyApi(http.Controller):
    # methods = ["POST"] when you do creation u should use method post
    @http.route("/v1/property", methods=["POST"], type="http", auth="none",csrf=False)
    def post_property(self):
        # wrote the data in postman, now want to get this data from postman to do creation
        args = request.httprequest.data.decode()
        # this mean I say after you get the data make this data json in variable vals
        vals = json.loads(args)
        # after that u will create  the  data  now, we used now sudo because we put auth = none
        res = request.env['property'].sudo().create(vals)
        # this for check if res created or no , if created will send me message
        if res:
            return request.make_json_response({
                "message": "property has been created"
            }, status=200)



























