from railway.src import avail,all_trains,booking,all_booked,cancel,register
from flask import render_template,url_for,flash
from flask import request, redirect
from railway.models import Users,Trains,Booking
from railway import forms
from railway import app
from flask_login import login_user,current_user,logout_user


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form  = forms.LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(uid = form.username.data).first()
        if user and user.password==form.password.data:
            login_user(user=user,remember=form.remember.data)
            flash(f'You are logged in!','success')
            return redirect(url_for('home'))
        
        flash(f'Login Unsuccessful','danger')

    return render_template('login.html',form = form)


@app.route('/register',methods=['GET','POST'])
def reg():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

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

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))