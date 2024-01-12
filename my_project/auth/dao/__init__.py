

from .customer.customer_dao import CustomerDao
from .composition.composition_dao import CompositionDao
from .composition.ingredients_dao import IngredientsDao
from .delivery.delivery_dao import DeliveryDao
from .delivery.delivery_method_dao import DeliveryMethodDao
from .menu.drinks_dao import DrinksDao
from .menu.pizzas_dao import PizzasDao
from .order.discount_dao import DiscountDao
from .order.order_dao import OrderDao
from .order.payment_dao import PaymentDao
from .order.review_dao import ReviewsDao

customer_dao = CustomerDao()
composition_dao = CompositionDao()
ingredients_dao = IngredientsDao()
delivery_dao = DeliveryDao()
delivery_method_dao = DeliveryMethodDao()
drinks_dao = DrinksDao()
pizzas_dao = PizzasDao()
discount_dao = DiscountDao()
order_dao = OrderDao()
payment_dao = PaymentDao()
review_dao = ReviewsDao()