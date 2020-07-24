## Example on how to use Prometheus and Grafana to monitor a Flask API application

Example deployment of a Flask API using Prometheus and Grafana for metrics and monitoring. All tied together using docker-compose.

### Install dependencies

```
pip install -r api/requirements.txt
```

### Set up and run everything using docker-compose

```
docker-compose up
```

### Access

* API: http://localhost:5000/flask-prometheus-grafana-example/
* Prometheus: http://localhost:9090/
* Grafana: http://localhost:3000 `[username: admin, password: pass@123]`
