from flask import Flask

def register_routes(app: Flask) -> None:

    from .order.order_route import order_bp
    from .order.discount_route import discount_bp
    from .order.payment_route import payment_bp
    from .order.review_route import review_bp
    from .menu.drinks_route import drinks_bp
    from .menu.pizzas_route import pizzas_bp
    from .delivery.delivery_route import delivery_bp
    from .delivery.delivery_method_route import delivery_method_bp
    from .customer.customer_route import customer_bp
    from .composition.composition_route import composition_bp
    from .composition.ingredients_route import ingredients_bp

    app.register_blueprint(order_bp)
    app.register_blueprint(discount_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(drinks_bp)
    app.register_blueprint(pizzas_bp)
    app.register_blueprint(delivery_bp)
    app.register_blueprint(delivery_method_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(ingredients_bp)
    app.register_blueprint(composition_bp)

