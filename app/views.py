from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user={'name':'chenchanglei'}
    post=[
      {
       'author':{'name':'zhangsan'},
       'body':'my name is zhangsan'
      },
      {
       'author':{'name':'lisi'},
       'body':'my name is lisi'
      }
    ]
    return render_template('index.html',title='',user=user,post=post)
	
