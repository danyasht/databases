
from my_project.auth.service.customer.customer_service import CustomerService
from my_project.auth.service.composition.composition_service import CompositionService
from my_project.auth.service.composition.ingredients_service import IngredientsService
from my_project.auth.service.delivery.delivery_service import DeliveryService
from my_project.auth.service.delivery.delivery_method_service import DeliveryMethodService
from my_project.auth.service.menu.drinks_service import DrinksService
from my_project.auth.service.menu.pizzas_service import PizzasService
from my_project.auth.service.order.discount_service import DiscountService
from my_project.auth.service.order.order_service import OrderService
from my_project.auth.service.order.payment_service import PaymentService
from my_project.auth.service.order.review_service import ReviewService

customer_service = CustomerService()
composition_service = CompositionService()
ingredients_service = IngredientsService()
delivery_service = DeliveryService()
delivery_method_service = DeliveryMethodService()
drinks_service = DrinksService()
pizzas_service = PizzasService()
discount_service = DiscountService()
order_service = OrderService()
payment_service = PaymentService()
review_service = ReviewService()
