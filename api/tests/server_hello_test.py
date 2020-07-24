import server


def test_server_hello(client):
    res = client.get('/flask-prometheus-grafana-example/')
    assert res.json == {'message': 'hello'}
