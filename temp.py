# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from scripts.labeled_property_graph import LabeledPropertyGraph

from faker import Faker
import random

def graphy():
    """Graph for testing."""
    lpg = LabeledPropertyGraph()
    faker = Faker()
    phone_nums = list(set([faker.phone_number() for _ in range(100)]))
    relations = list(set([faker.word() for _ in range(100)]))
    for number in phone_nums:
        lpg.add_node(number)
    for _ in range(250):
        name_a = random.choice(phone_nums)
        name_b = random.choice(phone_nums)
        relationship = random.choice(relations)
        both_ways = bool(random.getrandbits(1))
        try:
            lpg.add_relationship(relationship, name_a, name_b, both_ways)
        except ValueError:
            continue
    
    return lpg
