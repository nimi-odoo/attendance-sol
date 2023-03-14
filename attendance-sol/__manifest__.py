# -*- coding: utf-8 -*-

{
    'name': 'attendance',
    
    'summary': 'attendances modification poc',
    
    'description': """
        attendances display a dropdown (or some view) with sale order lines
    """,
    
    'author': 'Odoo',
    'licence': 'OEPL 1.0',
    'website': 'https://www.odoo.com',
    'license': 'OPL-1',
    'category': 'Learning',
    'version': '0.1',
    
    'depends': ['base', 'sale', 'hr_attendance', 'timesheet_grid'],
    
    'data': [
        "views/hr_attendance_views.xml"
    ],
    "assets": {
        "web.assets_backend": {
            "attendance-sol/static/src/js/kioskmode.js",
            "attendance-sol/static/src/js/kioskconfirm.js",
            "attendance-sol/static/src/xml/attendance.xml"
        }
    }
    
}
