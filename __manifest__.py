{
    'name': 'Student Face Attendance',

    'version': '1.0',

    'category': 'Education',

    'summary': 'AI Powered Face Attendance',

    'author': 'Aakash',

    'license': 'LGPL-3',

    'depends': [
        'base',
        'web'
    ],

    'data': [

        'security/ir.model.access.csv',

        'views/student_views.xml',
        'views/face_views.xml',
        'views/attendance_views.xml',
        'views/attendance_session_views.xml',
        'views/settings_views.xml',
        'views/menu_views.xml',

    ],

    'installable': True,

    'application': True,

    'auto_install': False,
}