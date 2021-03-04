import numpy as np
from client import *
import json
import requests

ID = "n3eEadyA2H45SSH97P9JCgWFqajNk8pvx086l1tVwFCEs9sPkT"

weights = [
      0.0,
      -1.9958774801473013e-12,
      -1.5745314999739934e-13,
      1.0224985382850534e-10,
      7.335138725679962e-10,
      -1.5803196211828163e-15,
      1.2427377416431243e-15,
      3.5464074071099316e-05,
      -2.309810765475757e-06,
      -1.294127326416192e-08,
      9.170608207768253e-10
    ]

errors = submit(ID, weights)

print(errors)