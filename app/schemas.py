from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal


class CategoryCreate(BaseModel):
	name: str = Field(min_length=2, max_length=50, description='Название категорий (3-50 символов)')
	parent_id: int | None = Field(None, description='ID родительской категорий, если есть')


class Category(BaseModel):
	id: int = Field(description='Уникальный идентификатор категорий')
	name: str = Field(description='Название категорий')
	parent_id: int | None = Field(None, description='ID родительской категории, если есть')
	is_active: bool = Field(description='Активность категории')

	model_config = ConfigDict(from_attributes=True)
