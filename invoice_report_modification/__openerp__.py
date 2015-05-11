{
    'name' : 'Modify Invoice Report',
    'version': '1.0',
    'summary': 'Modifies Invoice Report',
    'sequence': '19',
    'category': 'Tools',
    'complexity': 'easy',
    'description':
        """
Modify Report
=============

        """,
    'data': [
      'views/report_invoice.xml',
    ],
    'depends' : ['account','sale_layout'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
