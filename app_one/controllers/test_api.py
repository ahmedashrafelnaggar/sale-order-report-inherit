from odoo import http




class TestApi(http.Controller):

    @http.route("/api/test", methods=["Get"], type="http", auth="none",csrf=False)
    def test_endpoint(self, **kw):
        return "hi  ahmed"