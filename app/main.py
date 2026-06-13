from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import engine, Base
from app.models import Ticket
from app.dependencies import get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Support CRM")
templates = Jinja2Templates(directory="templates")


# Create database tables


@app.get("/ui", response_class=HTMLResponse)
def ui(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/")
def home():
    return {"message": "Welcome to the Support CRM System!"}


@app.post("/tickets")
def create_ticket(
    customer_name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    description: str = Form(...),
    db: Session = Depends(get_db)
):
    new_ticket = Ticket(
        customer_name=customer_name,
        email=email,
        subject=subject,
        description=description,
        status="Open"
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return {
        "message": "Ticket created successfully",
        "ticket_id": new_ticket.id
    }
@app.get("/tickets")
def get_all_tickets(db: Session = Depends(get_db)):
    tickets = db.query(Ticket).all()
    return tickets
@app.put("/tickets/{ticket_id}")
def update_ticket_status(
    ticket_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if ticket is None:
        return {"error": "Ticket not found"}

    ticket.status = status
    db.commit()
    db.refresh(ticket)

    return {
        "message": "Ticket status updated successfully",
        "ticket": ticket
    }
@app.delete("/tickets/{ticket_id}")
def delete_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if ticket is None:
        return {"error": "Ticket not found"}

    db.delete(ticket)
    db.commit()

    return {"message": "Ticket deleted successfully"}