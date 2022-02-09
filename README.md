# Basket Problem

#### Execution

> Note: Program requires python `3.6 or greater` to run.

Install the dependencies to generate coverage.

```sh
pip install -r requirements.txt
```

For program execution along with test cases.

```sh
python basket.py
```

Execute test cases.

```sh
python -m unittest basket.TestProduct
```
Execute coverage and view report.
```sh
> coverage run -m unittest basket.TestProduct
> coverage report
> coverage html
```


#### Explanation
```python
def __init__(self, product, delivery_rules, offer_rules) -> None:
```
above method is used to initialise the Basket object with required params :\
product -> a `dict` with key as `product_code` and value as `list` having first value as `product_name` and second as `cost` of single unit.
```python
{
    "R01": ["Red Widget", 32.95],
    "G01": ["Green Widget", 24.95],
    "B01": ["Blue Widget", 7.95]
}
```
delivery_rules -> a `dict` with rules having key as `cost` and value as `list` having `range of total_cost`.
```python
{4.95: [0, 49], 2.95: [50, 89]}
```
offer_rules -> a `dict` with key as `product_name` for which offer is valid and value as `list` having first index value as `rule` and second as applied `cost`
```python
{"R01": ["i%2==0", 32.95/2]}
```
some examples for valid rules - 
- `i%2==0, 32.95/2` => offer applicable for every even/second item and applicable cost would be half of original.
- `i%2==0, 0` => offer applicable for every even/second item and applicable cost would be 0 or free.

```python
def add_product_to_basket(self, product_code) -> None:
```
above method is used to add product to basket by passing valid product_code as param.

```python
def calculate_cost(self) -> str:
```
above method is used to calculate total_cost and return it upto 2 decimal place after round off.

```python
def empty_basket(self):
```
above method is used to clear/re-initialize basket.
