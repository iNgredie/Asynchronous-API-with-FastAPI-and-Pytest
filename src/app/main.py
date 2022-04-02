from fastapi import FastAPI

app = FastAPI()


@app.get('/ping')
async def pong():
    return {'ping': 'pong!'}


@app.get('/notes')
async def get_notes():
    return [
        {'note_1': 'first_note'},
        {'note_2': 'second_note'},
    ]
