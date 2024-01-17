## NoSQL explanation

This makes use of mongodb Atlas service for easy access to a mongodb cluster.

The database is then created on the mongodb Atlas using the UI and a connection url generated for use in mongodb compass client

Once a connection is connected

Once connected, a collection is created and in this case two collections were created

* station
* station-5000

`station` collection is the entire processed CSV file while `station-5000` is a limited subset of the processed CSV file with the first 5000 rows

The respective generated CSV files are then imported on the mongodb compass UI accordingly

### The queries
Starting with the station collection, the query executed was the equivalent of 

```
db.station.find({NO2: {$gte: 100}})
```
The screenshot of this query being station-NO2-gte-100-tabular.png attached has 1588 rows

while

```
db.station.find({NO2: {$gte: 100}}).limit(10)
```
The screenshot of this query being station-NO2-gte-100-tabular-limit-10.png attached has 10 rows

similarly,

```
db.station-5000.find({NO2: {$gte: 100}})
```
The screenshot of this query being station5000-NO2-gte-100-tabular.png attached has 351 rows

while

```
db.station-500.find({NO2: {$gte: 100}}).limit(10)
```
The screenshot of this query being station5000-NO2-gte-100-tabular-limit-10.png attached has 10 rows

Essentially, these queries fetch all the rows with NO2 greater than 100
