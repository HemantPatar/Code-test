# Code-test

Submitting coding exercise file as asked.

Here are some test results:-

1. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "Abhishek", "ExpirationDate": "03/21", "SecurityCode": "123","Amount": "3.00"}
Result - {"message": "Payment done from CheapPaymentGateway."}
Response - 200 | Method - 'POST'

2. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "Abhishek", "ExpirationDate": "03/2021", "SecurityCode": "123","Amount": "30.00"}
Result - {"message": "Payment done from CheapPaymentGateway."}
Response - 200 | Method - 'POST'


3. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "Abhishek", "ExpirationDate": "03/2021", "SecurityCode": "123","Amount": "35.00"}
Result - {"message": "Error while completing the payment process!!"}
Response - 400 | Method - 'POST' | Statement - Retring up to 3 times in case payment does not get processed.

4. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "Abhishek", "ExpirationDate": "03/2021", "SecurityCode": "123","Amount": "500.00"}
Result - {"message": "Error while completing the payment process!!"}
Response - 400 | Method - 'POST' | Statement - Retring up to 3 times in case payment does not get processed.

5. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "Abhishek", "ExpirationDate": "03/2021", "SecurityCode": "123","Amount": "500.00"}
Result - {"message": "Payment done from PremiumPaymentGateway."}
Response - 200 | Method - 'POST'

6. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "Abhishek", "ExpirationDate": "03/2021", "SecurityCode": "123","Amount": "10.00"}
Result - {"message": "Payment done from CheapPaymentGateway."}
Response - 200 | Method - 'POST'

7. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "Abhishek", "ExpirationDate": "03/2021", "SecurityCode": "123","Amount": "600.00"}
Result - {"message": "Payment done from PremiumPaymentGateway."}
Response - 200 | Method - 'POST'

8. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "Abhishek", "ExpirationDate": "03/2021", "SecurityCode": "123","Amount": "800.00"}
Result - {"message": "Error while completing the payment process!!"}
Response - 200 | Method - 'POST'

9. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "Abhishek", "ExpirationDate": "03/2021", "SecurityCode": "123","Amount": "30.00"}
Result - {"message": "Payment done from ExpensivePaymentGateway."}
Response - 200 | Method - 'POST'

10. Test sample - {"CreditCardNumber": "123412341234123", "CardHolder": "Abhishek", "ExpirationDate": "03/2021", "SecurityCode": "123","Amount": "800.00"}
Result - {"message": "Credit Card Number is not proper!!"}
Response - 400 | Method - 'POST'

11. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "", "ExpirationDate": "03/2021", "SecurityCode": "123","Amount": "800.00"}
Result - {"message": "Credit Card Holder's name not enterend!!"}
Response - 400 | Method - 'POST'

12. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "Abhishek", "ExpirationDate": "03/2019", "SecurityCode": "123","Amount": "800.00"}
Result - {"message": "Credit Card expiry date is not proper!!"}
Response - 400 | Method - 'POST'

13. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "Abhishek", "ExpirationDate": "03/2021", "SecurityCode": "","Amount": "800.00"}
Result - {"message": "Payment done from PremiumPaymentGateway."}
Response - 200 | Method - 'POST'

14. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "Abhishek", "ExpirationDate": "03/2021", "SecurityCode": "123","Amount": "80000"}
Result - {"message": "Amount not given properly!!"}
Response - 400 | Method - 'POST'

15. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "Abhishek", "ExpirationDate": "03/2021", "SecurityCode": "123","Amount": "-800.00"}
Result - {"message": "Negetive amount cannot be given!!"}
Response - 400 | Method - 'POST'

16. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "Abhishek", "ExpirationDate": "03/2020", "SecurityCode": "123","Amount": "800.00"}
Result - {"message": "Credit Card expiry date is not proper!!"}
Response - 400 | Method - 'POST'

17. Test sample - {"CreditCardNumber": "1234123412341234", "CardHolder": "Abhishek", "ExpirationDate": "03/2021", "SecurityCode": "123","Amount": "800.00"}
Result - {"message": "Internal Server Error"}
Response - 400 | Method - 'GET'
