

from my_project.auth.controller.customer.customer_controller import CustomerController
from my_project.auth.controller.composition.composition_controller import CompositionController
from my_project.auth.controller.composition.ingredients_controller import IngredientsController
from my_project.auth.controller.delivery.delivery_controller import DeliveryController
from my_project.auth.controller.delivery.delivery_method_controller import DeliveryMethodController
from my_project.auth.controller.menu.drinks_controller import DrinksController
from my_project.auth.controller.menu.pizzas_controller import PizzasController
from my_project.auth.controller.order.discount_controller import DiscountController
from my_project.auth.controller.order.order_controller import OrderController
from my_project.auth.controller.order.payment_controller import PaymentController
from my_project.auth.controller.order.review_controller import ReviewController

customer_service = CustomerController()
composition_service = CompositionController()
ingredients_service = IngredientsController()
delivery_service = DeliveryController()
delivery_method_service = DeliveryMethodController()
drinks_service = DrinksController()
pizzas_service = PizzasController()
discount_service = DiscountController()
order_service = OrderController()
payment_service = PaymentController()
review_service = ReviewController()

