from app import app, db
from flask import render_template, redirect, request
from models import Post, ContactForm
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import urllib.parse
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = urllib.parse.quote(request.form['name'])
        email = request.form['email']
        message = urllib.parse.quote(request.form['message'])
        msg = MIMEText(message, 'plain', _charset='utf-8')
        msg['Subject'] = Header('МК', 'utf-8')
        msg['From'] = XXX
        msg['To'] = email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(XXX, XXX)
        server.sendmail(msg['From'], email, msg.as_string())
        server.quit()
        return redirect('/')
    e_form = ContactForm()
    return render_template('index.html', e_form=e_form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/geo')
def geokvant():
    return render_template('GEO.html')

@app.route('/it')
def itkvant():
    return render_template('IT.html')

@app.route('/robo')
def robokvant():
    return render_template('ROBO.html')

@app.route('/ar_vr')
def arvrkvant():
    return render_template('VRAR.html')

@app.route('/create-article', methods=['POST','GET'])
def create_article():
    if request.method == 'POST':
        tit = request.form['title']
        text = request.form['text']
        art = Post(title=tit, text=text)
        
        db.session.add(art)
        db.session.commit()
        return redirect('/home')
            
    else:
        return render_template('create_article.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
