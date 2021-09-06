#!/usr/bin/env python
# coding: utf-8

# In[3]:


products = {
    5041 : {"pdt_name":"Cavin's Milkshake",     "pdt_price":240,  "stocks":35},
5042 : {"pdt_name":"Ashirwad ata",               "pdt_price":320,   "stocks":23},
5043 : {"pdt_name":"Mysore sandal soap",           "pdt_price":52,   "stocks":50},
5044 : {"pdt_name":"Lux international",         "pdt_price":38,   "stocks":30},
5045 : {"pdt_name":"Knor soap",       "pdt_price":30,  "stocks":40},
5046 : {"pdt_name":"Dark fantasy",   "pdt_price":150,  "stocks":20}
}


import json
js = json.dumps(products)
fd = open("products.json","w")
fd.write(js)
fd.close()

#read data from json

fd = open("products.json",'r')
r = fd.read()
fd.close()
products = json.loads(r)
products


prod_id = input("Enter the Product ID: ")
name = input("Enter the Name of the Product: ")
price = int(input("Enter the price per Item: "))
quan = int(input("Enter The Quantity of the Product you want to add: "))
products[prod_id] = {"pdt_name":name,"pdt_price":price,"stocks":quan}
js = json.dumps(products)
fd = open("products.json","w")
fd.write(js)
fd.close()

products


# In[ ]:




