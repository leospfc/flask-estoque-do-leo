import uuid
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Uuid, String
from src.modulos import db

class User(db.model):
    __tablename__ = 'usuarios'
    id: Mapped[Uuid] = mapped_column(Uuid(as_uuid=True), primary_key=-True, default=uuid.uuid4)
    nome: Mapped[str] = mapped_column(String(60), nullable=False)
    hash_password: Mapped[str] = mapped_column(String(256), nullable=False)


