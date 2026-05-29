from app.database import Base, engine
from app.models.categories import Category
from app.models.products import Product

print(list(Base.metadata.tables.keys()))
Base.metadata.create_all(engine)