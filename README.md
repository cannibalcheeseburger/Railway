# Railway Reservation system

This system is basically concerned with the reservation and cancellation of
railway tickets to the passengers. The need of this system arose because as is the
known fact that India has the largest railway network in the whole of the world
and to handle it manually is quite a tough job. By computerizing it, we will be
able to overcome many of its limitations and will be able to make it more efficient.
The handling of data and records for such a vast system is a very complex task if
done manually but it can be made much easier if the system is computerized. To
be more specific, our system is limited in such a way that a train starting from a
particular source will have a single destination.
## Authors

Names:
 - Kashish Srivastava (185014)
 - Karan Parmar (185013)
 - Rajat Thakur (185011)
 - Aakash (185016)
     
Course: CSD-327 Software Engineering LAB

Date: May 6th, 2021

Submitted to: Dr. Dharmendra Prasad Mahto
## Installation

### Build from Source

Clone the repository and checkout to stable commit

```
git clone https://github.com/cannibalcheeseburger/Railway.git
cd Railway
```

## Install Requirements

You need Python3 to run this  

For Linux:
```
sudo apt install python3
```

Install dependencies with:
```
pip install -r requirements.txt
```
or 
```
python3 -m pip install r -requirements.txt
```

## Usage

Change directory to `./Railway/` folder with

```
cd Railway
```

Run server with:

```
python3 manage.py runserver
```

Server will start at localhost:8000

Simply open:
```
http://127.0.0.1:8000/
```


## Admin Panel
Open admin panel at :
```
http://127.0.0.1:8000/admin
```

## References

[https://docs.djangoproject.com/en/3.2/](https://docs.djangoproject.com/en/3.2/)