from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.database import Base


class Category(Base):
	__tablename__ = 'categories'

	id: Mapped[int] = mapped_column(Integer, primary_key=True)
	name: Mapped[str] = mapped_column(String(50), nullable=False)
	is_active: Mapped[bool] = mapped_column(Boolean, default=True)
	parent_id: Mapped[int] = mapped_column(Integer, ForeignKey('categories.id'), nullable=True)

	products: Mapped[list['Product']] = relationship('Product', back_populates='category')

	parent: Mapped['Category'] = relationship('Category', remote_side=[id], back_populates='children')
	children: Mapped[list['Category']] = relationship('Category', back_populates='parent')