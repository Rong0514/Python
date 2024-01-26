import webbrowser
import importlib.util
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ECPay')
def ECPay():
    
    product_dict  = {'手機':1000 , '平板':2000 , '電腦':3000}

    '''商品名稱 與 商品價格 進行字串處理'''
    product_names = ''
    for name , price in zip(product_dict.keys() , product_dict.values()):  
        product_name ='#' + name + '__________' + str(price)
        product_names += product_name 

    '''計算商品總價格'''
    total_price   = 0
    for i in product_dict.values():
        total_price += int(i)    
    
    '''______________________________________________________1. 綠界金流sdk檔'''
    
    file_path = "ecpay_payment_sdk.py"
    spec      = importlib.util.spec_from_file_location("ecpay_payment_sdk", file_path)
    module    = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    '''___________________________________________________________2. 訂單資訊'''

    order_params = {
        'MerchantTradeNo'  : datetime.now().strftime("NO%Y%m%d%H%M%S"),       # 特店編號
        'StoreID'          : '',                                              # 特店訂單編號
        'MerchantTradeDate': datetime.now().strftime("%Y/%m/%d %H:%M:%S"),    # 特店交易時間
        'PaymentType'      : 'aio',                                           # 交易類型
        'TotalAmount'      : total_price,                                     # 交易金額
        'TradeDesc'        : '訂單測試',                                       # 交易描述
        'ItemName'         : product_names,                                   # 商品名稱
        'ReturnURL'        : 'https://www.ecpay.com.tw/return_url.php',       # 付款完成通知回傳網址
        'ChoosePayment'    : 'ALL',                                           # 選擇預設付款方式
        'ClientBackURL'    : 'http://127.0.0.1:5000/home',                    # Client端返回特店的按鈕連結
        'ItemURL'          : 'https://www.ecpay.com.tw/item_url.php',         # 商品銷售網址
        'Remark'           : '交易備註',                                       # 備註欄位
        'ChooseSubPayment' : '',                                              # 付款子項目
        'OrderResultURL'   : '',                                              # Client端回傳付款結果網址
        'NeedExtraPaidInfo': 'Y',                                             # 是否需要額外的付款資訊
        'DeviceSource'     : '',                                              #
        'IgnorePayment'    : '',                                              # 隱藏付款方式
        'PlatformID'       : '',                                              # 特約合作平台商代號
        'InvoiceMark'      : 'N',                                             # 
        'CustomField1'     : '',                                              # 自訂名稱欄位1
        'CustomField2'     : '',                                              # 自訂名稱欄位2
        'CustomField3'     : '',                                              # 自訂名稱欄位3
        'CustomField4'     : '',                                              # 自訂名稱欄位4
        'EncryptType'      :  1,                                              # 語系設定 ENG：英語 KOR：韓語 JPN：日語 CHI：簡體中文
        'Language'         : '',
    }
    
    extend_params_1 = {
        'ExpireDate': 7,
        'PaymentInfoURL': 'https://www.ecpay.com.tw/payment_info_url.php',
        'ClientRedirectURL': '',
    }
    extend_params_2 = {
        'StoreExpireDate': 15,
        'Desc_1': '',
        'Desc_2': '',
        'Desc_3': '',
        'Desc_4': '',
        'PaymentInfoURL': 'https://www.ecpay.com.tw/payment_info_url.php',
        'ClientRedirectURL': '',
    }
    extend_params_3 = {
        'BindingCard': 0,
        'MerchantMemberID': '',
    }
    extend_params_4 = {
        'Redeem': 'N',
        'UnionPay': 0,
    }
    inv_params = {
    }
    
    ecpay_payment_sdk = module.ECPayPaymentSdk(MerchantID='3002599',HashKey='spPjZn66i0OhqJsQ',
                                                HashIV='hT5OJckN45isQTTs')
    order_params.update(extend_params_1)
    order_params.update(extend_params_2)
    order_params.update(extend_params_3)
    order_params.update(extend_params_4)
    order_params.update(inv_params)

    try:
        final_order_params = ecpay_payment_sdk.create_order(order_params)
      
        action_url = 'https://payment-stage.ecpay.com.tw/Cashier/AioCheckOut/V5' 
        html = ecpay_payment_sdk.gen_html_post_form(action_url, final_order_params)
        
        return render_template('ECPay.html' , html = html)
        
    except Exception as error:
        print('An exception happened: ' + str(error))


@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000/ECPay")
    app.run(debug=False)


