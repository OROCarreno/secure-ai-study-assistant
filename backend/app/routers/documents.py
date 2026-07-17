from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.document import Document
from app.schemas.document import DocumentCreate, DocumentResponse
from typing import List

router = APIRouter(prefix="/documents", tags=["documents"])

@router.post("/", response_model=DocumentResponse)
def create_document(doc: DocumentCreate, owner_id: int, db: Session = Depends(get_db)):
    new_doc = Document(title=doc.title, content=doc.content, owner_id=owner_id)
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc

@router.get("/", response_model=List[DocumentResponse])
def list_documents(owner_id: int, db: Session = Depends(get_db)):
    # SECURITY: filter by owner_id — users only see their own documents
    return db.query(Document).filter(Document.owner_id == owner_id).all()

@router.delete("/{doc_id}")
def delete_document(doc_id: int, owner_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(
        Document.id == doc_id,
        Document.owner_id == owner_id  # SECURITY: verify ownership
    ).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    db.delete(doc)
    db.commit()
    return {"message": "Document deleted"}