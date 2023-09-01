from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Define a route to handle PayPal webhook events
@app.route('/paypal/webhook', methods=['POST'])
def paypal_webhook():

    # Verify the incoming request is from PayPal
    # (You need to implement the verification logic)

    # Parse the incoming JSON payload
    payload = request.json
    print("*****Webhook payload starts here********")
    print(payload)
    print("*****Webhook payload ends here********")
    ##logging.basicConfig(filename='whevent.log',level=logging.DEBUG)
    # Handle the PayPal event based on the event type
    event_type = payload['event_type']
    if event_type == 'CHECKOUT.ORDER.VOIDED':
        # Handle completed payment capture event
        # Extract relevant information from payload

    # Respond to PayPal with a 200 OK
        return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run()
