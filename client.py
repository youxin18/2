import requests

json_data = {'a': 1, 'b': 2}

r = requests.post("http://127.0.0.1:5000/add", json=json_data)

print(r.text)


@app.route('/register', methods=['POST'])
def register():
    print(request.headers)
    print(request.stream.read())
    result = {"out_trade_no":"000000","total_charge":"1000","access_token":"1","async_callback_url":"a","product_id":"0001","product_name":"刀","product_amount":"100","product_desc":"工具","rate":"1:1","role_id":"0011","role_name":"yxzjz","server_id":"29区","extend":"a","union_extend":"aa","currency_code":"RMB","pay_type":"weixin","order_no":"1"}
    return result