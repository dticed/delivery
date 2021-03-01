

# teste de app
def test_app_is_created(app):
    assert app.name == "delivery.app"
    
# teste de config
def test_config_is_loaded(config):
    assert config['DEBUG'] is False
    
# teste de client
def test_request_returns_404(client):
    assert client.get('/url_que_nao_existe').status_code == 404
    
def test_request_returns_200(client):
    assert client.get('/').status_code == 200
    
    