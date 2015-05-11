{
    'name' : 'Modify Sale Order Report',
    'version': '1.0',
    'summary': 'Modifies Sale Order Report',
    'sequence': '19',
    'category': 'Tools',
    'complexity': 'easy',
    'description':
        """
Modify Report
=============

        """,
    'data': [
      'views/report_saleorder.xml',
    ],
    'depends' : ['sale','sale_layout'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
