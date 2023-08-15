import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Language(SQLModel, table=True):
    
    __tablename__ = "Languages"
    
    id_language: Optional[int] = Field(primary_key=True)
    language_name: str = Field(
        nullable=False,
        description="Nombre en texto del lenguaje."
    )
    language_code: int = Field(
        nullable=False,
        description="Codigo del lenguaje (ES, EN)"
    )
    native_name: str = Field(
        nullable=False,
        description="El nombre del idioma en su forma nativa (Español -> Spanish)."
    )
    is_default: bool = Field(
        nullable=False,
        default=False,
        description="Indicador que indica que si es el lenguaje por defecto de la app."
    )
    created_at: datetime = Field(nullable=False, default=datetime.datetime.now())
    updated_at: datetime = Field(nullable=False, default=datetime.datetime.now())
    

