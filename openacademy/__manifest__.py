{
    'name':"Open Academy",
'sammary' : """ manage trianings """,
    'description':
        """
        Open Academy medule for managing trianings
   - training courses
   - training sessions
   - attendees registration
        """,
    'author':"Hazem Mahmoud",
    'webside':"http://www.yourcompany.com",
   ' category':'test',
    'version':'0.1',
 'depends': ['base', 'board'],
'data': [
'security/security.xml',
'security/ir.model.access.CSV',
'views/openacademy.xml',
'views/partner.xml',
'views/session_board.xml'

 # 'templates.xml',
],
 'demo':['demo.xml',],
}