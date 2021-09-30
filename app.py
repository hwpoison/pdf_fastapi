from fastapi import FastAPI
from fastapi.responses import FileResponse
from services.invoice import invoice

app = FastAPI()


@app.get('/ticket')
async def generate_ticket(title: str) -> FileResponse:
    pdf_path = invoice({
        'details': {'title': title, 'ticket_num': 30412},
        'items': {
            'ITEM 1': 300.0,
            'ITEM2': 500.0,
            'ITEM 3': 700.0,
            'ITEM 3': 343.12
        }
    })
    return FileResponse(
        path=pdf_path,
        headers={
            'Content-Disposition': f'inline;filename="{pdf_path.stem}.pdf"'
        },
        media_type='application/pdf')
