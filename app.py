from src import avail,all_trains,booking,all_booked,cancel
from flask import Flask
from flask import render_template
from flask import request, redirect


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/all')
def allTrains():
    rows = all_trains.all_trains()
    return render_template('all.html',rows = rows)

@app.route('/avail',methods=['POST','GET'])
def available():
    if request.method == 'POST': 
        dat = request.form['date']
        rows = avail.Avail(dat)
        return render_template('avail.html',rows=rows)
    else:
        return render_template('avail.html')

@app.route('/all_booked')
def booked():
    rows = all_booked.all_book()
    return render_template('all_booked.html',rows = rows)

@app.route('/book',methods = ['POST','GET'])
def bookings():
    if request.method == 'POST': 
        tid = request.form['train_id']
        count = int(request.form['count'] )      
        rows = booking.book(tid,count)
        return render_template('book.html',rows=rows,tot = count*rows[6])
    else:
        return render_template('book.html')

@app.route('/cancel')
def cancelling():
    rows = all_trains.all_trains()
    return render_template('home.html',rows = rows)


if __name__ == "__main__":
    app.run(debug = True)

