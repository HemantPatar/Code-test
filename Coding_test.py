from flask import Flask, Response, request
import json, datetime, random

app = Flask(__name__)
app.config['DEBUG'] = True


class UserApi(object):
    @staticmethod
    def post():
        data = request.get_json()
        message, status = ProcessPayment(data["CreditCardNumber"], data["CardHolder"], data["ExpirationDate"], data["SecurityCode"], data["Amount"])
        return Response(message, status=status, mimetype="application/json")
    def get():
        message, status = json.dumps({"message": "Internal Server Error"}), 500
        return Response(message, status=status, mimetype="application/json")



def ProcessPayment(ccnumber, ccholder, expdate, scode, amount):
    chk = str(datetime.datetime.now()).split("-")
    if len(ccnumber) < 16: 
        return json.dumps({"message": "Credit Card Number is not proper!!"}), 400
    if ccholder is "":
        return json.dumps({"message": "Credit Card Holder's name not enterend!!"}), 400
    expdate = expdate if len(expdate.split('/')[1]) == 4 else expdate.split("/")[0]+"/20"+expdate.split('/')[1]
    if int(expdate.split('/')[1]) <= int(chk[0]) and int(expdate.split("/")[0]) <= int(chk[1]): 
        return json.dumps({"message": "Credit Card expiry date is not proper!!"}), 400
    if "." not in amount : 
        return json.dumps({"message": "Amount not given properly!!"}), 400
    elif float(amount) < 0: 
        return json.dumps({"message": "Negetive amount cannot be given!!"}), 400
    
    if float(amount) < 20: 
        return json.dumps({"message": "Payment done from CheapPaymentGateway."}), 200
    elif 21 < float(amount) < 500:
        if random.randint(1, 10) % 2 == 0: 
            return json.dumps({"message": "Payemnt done from ExpensivePaymentGateway."}), 200
        else: 
            return json.dumps({"message": "Payment done from CheapPaymentGateway."}), 200
    else: 
        for i in range(3):
            if i == 2: 
                return json.dumps({"message": "Error while completing the payment process!!"}), 400
            else: 
                if random.randint(1, 10) % 2 == 0:
                    return json.dumps({"message": "Payment done from PremiumPaymentGateway."}), 200
                    break
                else: pass


app.add_url_rule("/", view_func=UserApi.post, methods=['POST'])
app.add_url_rule("/", view_func=UserApi.get, methods=['GET'])
app.run()