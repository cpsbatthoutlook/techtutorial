from app import app
@app.route('/a')
@app.route('/index')
def index1():
    user = {'username': 'Chander'}
    return '''
    <html> <head> <title> Home Page  </title>
        </head>
    <body>
        Hello,  
        ''' + user['username']  + '''
    </body>
    </html>
       
    
    
    '''