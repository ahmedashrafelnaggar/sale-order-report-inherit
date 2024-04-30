{
    'name': "Custom Sale Report",

    'summary': "",

    'description': """
    """,

    'author': "Ahmed Ashraf Elnaggar",
    'website': "",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': '',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_management'],
    'sequence':-100,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/sale_order_view.xml',
        'reports/sale_order_report.xml',

    ],
    'assets': {
        'web.report_assets_common': ['sale_order_report/static/src/css/sale_order_report.css'],

    },
    # only loaded in demonstration mode
    'demo': [
    ],
    'application':True,
    'auto_install':False,
}