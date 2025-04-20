from fastapi import FastAPI


app = FastAPI()

@app.get("/home/")
def get_articles():
    articles = [
        {
            'id': 1,
            'name': 'first article',
            'date': 'August 7, 2024'
        },
        {
            'id': 2,
            'name': 'second article',
            'date': 'August 7, 2024'
        },
        {
            'id': 3,
            'name': 'third article',
            'date': 'August 7, 2024'
        },
    ] 
    return articles




