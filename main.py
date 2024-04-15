from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/payroll/", response_class=HTMLResponse)
async def renderHtml():
    return """
    <html>
        <head>
            <title>Payroll</title>
        </head>
        <body>
            <h1>Payroll</h1>
        </body>
    </html>
    """
