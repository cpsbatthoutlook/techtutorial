from app import app
@app.route('/a')
@app.route('/index')
def index1():
    return 'Hello, World-1!!'