import os

from api import app




if __name__ == '__main__':
    app.debug = True
    app.config['DATABASE_HOST'] = 'mongodb://localhost:27017'
    app.config['DATABASE_NAME'] = 'personal_cv'
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
