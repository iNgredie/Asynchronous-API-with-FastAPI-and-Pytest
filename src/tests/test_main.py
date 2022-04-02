def test_ping(test_app):
    response = test_app.get('/ping')
    assert response.status_code == 200
    assert response.json() == {'ping': 'pong!'}


def test_notes(test_app):
    response = test_app.get('/notes')
    assert response.status_code == 200
    assert response.json() == [
        {'note_1': 'first_note'},
        {'note_2': 'second_note'},
    ]
