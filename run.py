from flask import Flask, render_template, request, redirect, url_for
from azuredbf import AzureDB  # Assuming AzureDB class is in azuredb.py
from datetime import datetime

app = Flask(__name__)

# Database configuration
azure_db = AzureDB()


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
 return render_template('contact.html')


@app.route('/guests', methods=['GET', 'POST'])
def guest():
    if request.method == 'POST':
        if 'nickname' in request.form and 'text' in request.form:
            nickname = request.form['nickname']
            text = request.form['text']


            if azure_db.azureAddData(nickname, text):
                return redirect(url_for('guest'))
            else:
                return "Failed to add data to database!"

        elif 'edit_btn' in request.form:
            guest_id = request.form['edit_btn']


        elif 'delete_btn' in request.form:
            guest_id = request.form['delete_btn']
            if azure_db.azureDeleteData(guest_id):
                return redirect(url_for('guest'))
            else:
                return "Failed to delete entry from database!"


    guests = azure_db.azureGetData()

    return render_template('guestlist.html', guests=guests)





@app.route('/guests/delete/<int:id>', methods=['POST'])
def delete_guest(id):

    if azure_db.azureDeleteData(id):
        return redirect(url_for('guest'))
    else:
        return "Failed to delete entry from database!"


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
