import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Theme(SQLModel, table=True):
    __tablename__ = "Themes"

    id_theme: Optional[int] = Field(primary_key=True)
    id_user: int = Field(nullable=False)
    primary_color: str = Field(
        nullable=False,
        description="El color principal o predominante del tema (puede ser un código hexadecimal).",
    )
    secondary_color: str = Field(
        nullable=False,
        description="Un color secundario o de resalte para el tema (puede ser un código hexadecimal).",
    )
    tertiary_color: str = Field(
        nullable=False,
        description="Un color terciario o de resalte para el tema (puede ser un código hexadecimal).",
    )
    theme_name: str = Field(nullable=False, description="Nombre del tema.")
    background_color: str = Field(nullable=False, description="Nombre del tema.")
    font_color: str = Field(nullable=False, description="Nombre del tema.")
    created_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )
    updated_at: datetime.datetime = Field(
        nullable=False, default=datetime.datetime.now()
    )
