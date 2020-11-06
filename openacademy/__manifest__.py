{
    "name": "Open Academy",
    "summary": """
       Open Academy module for managing trainings:
       - training courses
       - training sessions
       - attendees registration
       """,
    "author": "Vauxoo,Odoo Community Association (OCA)",
    "website": "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml # noqa
    # for the full list
    "category": "Uncategorized",
    "version": "13.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/views.xml",
        "views/templates.xml",
        "views/partner.xml",
        "reports.xml",
    ],
    # only loaded in demonstration mode
    "demo": ["demo/demo.xml"],
    "license": "AGPL-3",
}
