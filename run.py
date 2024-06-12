from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'exapmle@gamil.com'
app.config['MAIL_PASSWORD'] = '123123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aboutme')
def about_me():
    return render_template('aboutme.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        msg = Message("Hello, I'm from Portfolio!", sender='noreply@demo.com', recipients=['daniilmazurenko2204@gmail.com'])
        msg.body = "Hey, how are you? Is everything okay?"
        mail.send(msg)
        return "Email sent!"
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)