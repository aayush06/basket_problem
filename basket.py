# =============================================================================
# Created By  : Aayush Bhatnagar (aayushbhatnagar06@gmail.com)
# =============================================================================

import unittest


class TestProduct(unittest.TestCase):
    """
        Testcase class to test Basket class
    """
    def setUp(self) -> None:
        self.basket1 = Basket({                  # product catalog
            "R01": ["Red Widget", 32.95],
            "G01": ["Green Widget", 24.95],
            "B01": ["Blue Widget", 7.95]
            },
            {4.95:[0,49],2.95:[50, 89]},        # delivery rule where cost is 4.95 when total_cost is b/w 0-49.9 and 2.95 when total_cost is b/w 50-89.9
            {"R01": ["i%2==0", 32.95/2]}        # offers rule where product with code R01 every even product is of half cost
        )

        self.basket2 = Basket({                  # product catalog
            "R01": ["Red Widget", 32.95],
            "G01": ["Green Widget", 24.95],
            "B01": ["Blue Widget", 7.95]
            },
            {4.95:[0,45],2.95:[46, 89]},        # delivery rule where cost is 4.95 when total_cost is b/w 0-45.9 and 2.95 when total_cost is b/w 46-89.9
            {
                "R01": ["i%2==0", 32.95/2],     # offers rule where product with code R01 every even product is of half cost and product with code G01 every even product is free
                "G01": ["i%2==0", 0]
            }        
        )

    def test_calculate_cost(self):
        """
            method to test total cost calculation based on various products added in basket1
        """
        # basket1 test cases
        self.basket1.add_product_to_basket("B01")
        self.basket1.add_product_to_basket("G01")
        self.assertEqual('37.85', self.basket1.calculate_cost())
        self.basket1.empty_basket()
        self.basket1.add_product_to_basket("R01")
        self.basket1.add_product_to_basket("R01")
        self.assertEqual('54.38', self.basket1.calculate_cost())
        self.basket1.empty_basket()
        self.basket1.add_product_to_basket("R01")
        self.basket1.add_product_to_basket("G01")
        self.assertEqual('60.85', self.basket1.calculate_cost())
        self.basket1.empty_basket()
        self.basket1.add_product_to_basket("B01")
        self.basket1.add_product_to_basket("B01")
        self.basket1.add_product_to_basket("R01")
        self.basket1.add_product_to_basket("R01")
        self.basket1.add_product_to_basket("R01")
        self.assertEqual('98.28', self.basket1.calculate_cost())

        #basket2 test cases
        self.basket2.add_product_to_basket("B01")
        self.basket2.add_product_to_basket("G01")
        self.assertEqual('37.85', self.basket2.calculate_cost())
        self.basket2.empty_basket()
        self.basket2.add_product_to_basket("G01")
        self.basket2.add_product_to_basket("G01")
        self.assertEqual('29.90', self.basket2.calculate_cost())
        self.basket2.empty_basket()
        self.basket2.add_product_to_basket("R01")
        self.basket2.add_product_to_basket("R01")
        self.assertEqual('52.38', self.basket2.calculate_cost())
        self.basket2.empty_basket()
        self.basket2.add_product_to_basket("G01")
        self.basket2.add_product_to_basket("G01")
        self.basket2.add_product_to_basket("R01")
        self.basket2.add_product_to_basket("R01")
        self.basket2.add_product_to_basket("R01")
        self.basket2.add_product_to_basket("G01")
        self.assertEqual('132.28', self.basket2.calculate_cost())




class Basket:
    def __init__(self, product, delivery_rules, offer_rules) -> None:
        """
            constructor to initialise Product object
            with product details and various rules
        """
        self.products = product
        self.basket1 = []
        self.delivery_rules = delivery_rules
        self.offers = offer_rules
        self.product_count_map = {}
        for k, v in product.items():
            self.product_count_map[k] = 0

    def add_product_to_basket(self, product_code) -> None:
        """
            method to add product to basket1
        """
        if product_code in self.products:
            self.basket1.append(product_code)
    
    def calculate_cost(self) -> str:
        """
            method that calculates cost based on added products, delivery rules and offers
        """
        total_cost = 0
        for i in self.basket1:
            self.product_count_map[i] += 1
        for key, val in self.product_count_map.items():
            if key in self.offers:
                for i in range(1, val+1):
                    if eval(self.offers[key][0]):
                        total_cost += self.offers[key][1]
                    else:
                        total_cost += self.products[key][1]
            else:
                total_cost += val*self.products[key][1]
        for k, v in self.delivery_rules.items():
            if int(total_cost) in range(v[0], v[1]+1):
                total_cost += k
                break
        return format(total_cost, '.2f')
    
    def empty_basket(self):
        self.basket1 = []
        for k, v in self.products.items():
            self.product_count_map[k] = 0


if __name__ == '__main__':
    basket1 = Basket({                  # product catalog
        "R01": ["Red Widget", 32.95],
        "G01": ["Green Widget", 24.95],
        "B01": ["Blue Widget", 7.95]
        },
        {4.95:[0,49],2.95:[50, 89]},        # delivery rule where cost is 4.95 when total_cost is b/w 0-49.9 and 2.95 when total_cost is b/w 50-89.9
        {"R01": ["i%2==0", 32.95/2]}        # offers rule where product with code R01 every even product is of half cost
    )
    basket1.add_product_to_basket("B01")
    basket1.add_product_to_basket("G01")
    total_cost = basket1.calculate_cost()
    print(total_cost)
    unittest.main()
