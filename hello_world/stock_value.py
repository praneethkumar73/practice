holding = [
{
"id": 419,

"stock id": 345,
 "type": "stock",

"symbol": "TSLA",

"price": 923.05,
 "value": 59998.25,

"quantity":65,
},
{

"id": 419,

"stock_id": 145,

"type": "stock",

"symbol": "AAPL",

"price": 143.85,

"value": 36106.35,

"quantity": 251,
},
{

"id": 419,

"stock_id": 123,

"type": "stock",

"symbol":"NVDA",
"price":235.09,
"Value": 10579.05,
"quantity":45,
}
]

x=(holding[0]['price']*holding[0]['quantity'])
y=(holding[1]['price']*holding[1]['quantity'])
z=(holding[2]['price']*holding[2]['quantity'])
print(x+y+z)