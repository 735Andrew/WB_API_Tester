import sqlalchemy as sa
import sqlalchemy.orm as so


class Base(so.DeclarativeBase):
    pass


class Sales(Base):
    __tablename__ = "sales"

    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    date: so.Mapped[str] = so.mapped_column(sa.String(64))
    nmId: so.Mapped[int] = so.mapped_column(sa.Integer)
    price: so.Mapped[float] = so.mapped_column(sa.Float)
