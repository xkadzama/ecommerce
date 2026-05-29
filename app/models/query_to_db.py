from app.database import SessionLocal
from app.models.categories import Category
from app.models.products import Product


# with SessionLocal() as session:
# 	stmt = Category(name='Одежда')
# 	session.add(stmt)
# 	session.commit()


# with SessionLocal() as session:
# 	category = session.query(Category).filter_by(name='Одежда').first()
# 	if category:
# 		product = Product(
# 			name='Пояс Dolce&Gabbana',
# 			description='Из крокодиловой кожи чьих маму и папу убили браконьеры',
# 			price=850,
# 			stock=2
# 		)
# 		category.products.append(product)
# 		session.add(product)
# 		session.commit()


with SessionLocal() as session:
	category = session.query(Category).filter_by(name='Техника').first()
	for product in category.products:
		print('-'*30)
		print(product.name)
		print(product.description)
		print(str(product.price) + '$')
		print('-' *30)



