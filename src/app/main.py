from fastapi import FastAPI, Response, status

app = FastAPI()

notes = [
    {'note_1': 'first_note'},
    {'note_2': 'second_note'},
]


@app.get('/ping')
async def pong():
    return {'ping': 'pong!'}


@app.get('/notes')
async def get_notes():
    return notes


@app.get('/note/{note_id}')
async def get_note(note_id: int):
    return notes[note_id]


@app.post('/notes')
async def create_notes(notes_data: dict):
    return notes_data


@app.put('/note/{note_id}')
async def update_note(note_id: int, notes_data: dict):
    notes[note_id] = notes_data
    return notes[note_id]


@app.delete('/note/{note_id}')
async def delete_note(note_id: int):
    notes.pop(note_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
