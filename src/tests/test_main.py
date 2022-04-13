def test_ping(test_app):
    response = test_app.get('/ping')
    assert response.status_code == 200
    assert response.json() == {'ping': 'pong!'}


def test_get_notes(test_app):
    response = test_app.get('/notes')
    assert response.status_code == 200
    assert response.json() == [
        {'note_1': 'first_note'},
        {'note_2': 'second_note'},
    ]


def test_get_note(test_app):
    notes = [
        {'note_1': 'first_note'},
        {'note_2': 'second_note'},
    ]
    response = test_app.get(f'/note/{1}')
    assert response.status_code == 200
    assert response.json() == notes[1]


def test_create_notes(test_app):
    response = test_app.post('/notes', json={'new_1': 'new_data_1'})
    assert response.status_code == 200
    assert response.json() == {'new_1': 'new_data_1'}


def test_update_note(test_app):
    response = test_app.put(f'/note/{1}', json={'new_1': 'new_data_1'})
    assert response.status_code == 200
    assert response.json() == {'new_1': 'new_data_1'}


def test_delete_note(test_app):
    response = test_app.delete(f'/note/{1}')
    assert response.status_code == 204
