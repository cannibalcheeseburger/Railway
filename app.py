from src import avail,all_trains,booking,all_booked,cancel,register
from flask import Flask,flash
from flask import render_template,url_for
from flask import request, redirect
import forms


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form  = forms.LoginForm()
    if form.validate_on_submit():
        flash(f'You have logged in!','success')
        #register.Reg(form.username.data,form.password.data)
        return redirect(url_for('home'))
    return render_template('login.html',form = form)


@app.route('/register',methods=['GET','POST'])
def reg():
    form  = forms.RegisterForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        #register.Reg(form.username.data,form.password.data)
        return redirect(url_for('home'))
    return render_template('Register.html',form = form)


@app.route('/all')
def allTrains():
    rows = all_trains.all_trains()
    return render_template('all.html',rows = rows)

@app.route('/avail',methods=['POST','GET'])
def available():
    form = forms.AvailForm()
    if form.is_submitted():
        rows = avail.Avail(form.date.data)
        return render_template('avail.html',rows=rows,form=form)
    return render_template('avail.html',form=form)

@app.route('/all_booked')
def booked():
    rows = all_booked.all_book()
    return render_template('all_booked.html',rows = rows)

@app.route('/book',methods = ['POST','GET'])
def bookings():
    form = forms.BookForm()
    if form.is_submitted():     
        rows = booking.book(form.train_id.data,int(form.count.data))
        return render_template('bookings.html',rows=rows,tot = int(form.count.data)*rows[6],form = form)
    else:
        return render_template('bookings.html',form = form)

@app.route('/cancel')
def cancelling():
    rows = all_trains.all_trains()
    return render_template('home.html',rows = rows)


if __name__ == "__main__":
    app.run(debug = True,port=8000)

