from fastapi import FastAPI

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


@app.get('/note/{id}')
async def get_note(note_id: int):
    return notes[note_id]
