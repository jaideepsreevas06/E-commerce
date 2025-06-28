from website import create_app, db
from website.models import Product

app = create_app()

with app.app_context():
    p1 = Product(name="Fresh Bananas", price=80.0, image="products/banana.jpeg")  # type: ignore
    p2 = Product(name="MacBook Air", price=120000.0, image="products/macbook.jpg")  # type: ignore
    p3 = Product(name="AirPods Pro", price=25000.0, image="products/airpods.jpeg")  # type: ignore
    p4 = Product(name="Apple Watch", price=45000.0, image="products/watch.jpeg")  # type: ignore
    p5 = Product(name="Casio Watch", price=8200.0, image="products/casiowatch.jpeg")  # type: ignore
    p6 = Product(name="Fresh Cherries", price=120.0, image="products/cherry.jpeg")  # type: ignore
    p7 = Product(name="Fresh Kiwis", price=524.0, image="products/kiwi.jpeg")  # type: ignore
    p8 = Product(name="Fresh Lemons", price=50.0, image="products/lemons.jpeg")  # type: ignore
    p9 = Product(name="Fresh Oranges", price=80.0, image="products/orange.jpeg")  # type: ignore
    p10 = Product(name="Fresh Pineapples", price=150.0, image="products/pineapple.jpeg")  # type: ignore
    p11 = Product(name="Fresh Pomegranates", price=200.0, image="products/pomegranate.jpeg")  # type: ignore
    p12 = Product(name="Fresh Strawberries", price=300.0, image="products/strawberry.jpeg")  # type: ignore
    p13 = Product(name="Allen Solly T-Shirt", price=1200.0, image="products/allensollytashirt.webp")  # type: ignore
    p14 = Product(name="Puma T-Shirt", price=1500.0, image="products/pumatshirt.webp")  # type: ignore
    p15 = Product(name="Puma Slides", price=800.0, image="products/pimaslide.jpeg")  # type: ignore
    p16 = Product(name="Skylona Shoes", price=2500.0, image="products/skylona.jpeg")  # type: ignore
    p17 = Product(name="Sparx Slippers", price=600.0, image="products/sparxslippers.jpg")  # type: ignore
    p18 = Product(name="Titan Watch", price=15000.0, image="products/titan.jpeg")  # type: ignore
    p19 = Product(name="Choki Choki", price=300.0, image="products/chokichoki.jpg")  # type: ignore
    p20 = Product(name="Dark Fantasy", price=102.0, image="products/darkfantasy.webp")  # type: ignore
    p21 = Product(name="Fuse", price=98.0, image="products/fuse.webp")  # type: ignore
    p22 = Product(name="Munch", price=161.0, image="products/munch.webp")  # type: ignore

    db.session.add_all([p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22])
    db.session.commit()
    print("Products added successfully!")
