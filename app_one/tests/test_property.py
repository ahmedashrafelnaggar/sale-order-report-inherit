from odoo.tests.common import TransactionCase
from odoo import fields


class TestProperty(TransactionCase):

    def setUp(self,*args,**kwargs):
        super(TestProperty, self).setUp()

    # This for create value
    #     self.property_01_record this is the name of record elly i created it
        self.property_01_record = self.env['property'].create({
            'ref':'PRT1000',
            'name': 'property 1000',
            'description': 'property description ',
            'post_code': '1010',
            # when you use field you should do import for fields
            'date_availability': fields.Date.today(),
            'expected_price': '1000',
        })

    # This  method for test values beta3et property elly created it now
    # i told him i do test for this record did it create or no ?
    def test_01_property_values(self):

        # property_id = self. name of  variable record who  i created it

        property_id = self.property_01_record

        # then stage check its mean did property_id = the same values or no ?
        # assertRecordValues this fixed (did property_id = [{
        # 'ref': 'PRT1000',
        # 'name': 'property 1000',
        # 'description': 'property description ',
        # 'post_code': '1010',
        # 'date_availability': fields.Date.today(),
        # 'expected_price': '1000',
        # }])
        self.assertRecordValues(property_id, [{
            'ref': 'PRT1000',
            'name': 'property 1000',
            'description': 'property description ',
            'post_code': '1010',
            'date_availability': fields.Date.today(),
            'expected_price': '1000',

        }])

        # then you should put this in edit configuration   --test-enable behind name of your app
        # -c odoo.conf -u app_one --test-enable

