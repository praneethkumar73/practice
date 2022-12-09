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
"value": 10579.05,
"quantity":45,
}
]

x=(holding[0]['price']*holding[0]['quantity'])
y=(holding[1]['price']*holding[1]['quantity'])
z=(holding[2]['price']*holding[2]['quantity'])
print ("stock price is :")
print(x+y+z)

a=(holding[0]['symbol'],holding[0]['value'])
b=(holding[1]['symbol'],holding[1]['value'])
e=(holding[2]['symbol'],holding[2]['value'])

newlist=[a,b,e]
print(newlist)

maxPrice = max(holding, key=lambda x:x['value'])
print('The stock TSLA that has more price value:'), print(maxPrice['value'])

