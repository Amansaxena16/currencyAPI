from flask import Flask, request, jsonify

app = Flask(__name__)

EXCHANGE_RATES = {
  "USD": {
    "EUR": 0.92,
    "GBP": 0.78,
    "INR": 82.64,
    "AUD": 1.50,
    "CAD": 1.35,
    "JPY": 134.50,
    "CHF": 0.92,
    "CNY": 7.12
  },
  "EUR": {
    "USD": 1.09,
    "GBP": 0.85,
    "INR": 89.85,
    "AUD": 1.63,
    "CAD": 1.47,
    "JPY": 146.50,
    "CHF": 1.00,
    "CNY": 7.75
  },
  "GBP": {
    "USD": 1.28,
    "EUR": 1.17,
    "INR": 104.56,
    "AUD": 1.91,
    "CAD": 1.60,
    "JPY": 172.50,
    "CHF": 1.18,
    "CNY": 9.12
  },
  "INR": {
    "USD": 0.012,
    "EUR": 0.011,
    "GBP": 0.0096,
    "AUD": 0.017,
    "CAD": 0.016,
    "JPY": 1.29,
    "CHF": 0.011,
    "CNY": 0.073
  },
  "AUD": {
    "USD": 0.67,
    "EUR": 0.61,
    "GBP": 0.52,
    "INR": 58.10,
    "CAD": 0.91,
    "JPY": 90.20,
    "CHF": 0.63,
    "CNY": 4.51
  },
  "CAD": {
    "USD": 0.74,
    "EUR": 0.68,
    "GBP": 0.62,
    "INR": 61.90,
    "AUD": 1.10,
    "JPY": 98.50,
    "CHF": 0.67,
    "CNY": 4.95
  },
  "JPY": {
    "USD": 0.0074,
    "EUR": 0.0068,
    "GBP": 0.0058,
    "INR": 0.77,
    "AUD": 0.011,
    "CAD": 0.010,
    "CHF": 0.0066,
    "CNY": 0.050
  },
  "CHF": {
    "USD": 1.09,
    "EUR": 1.00,
    "GBP": 0.85,
    "INR": 89.15,
    "AUD": 1.60,
    "CAD": 1.47,
    "JPY": 151.10,
    "CNY": 7.72
  },
  "CNY": {
    "USD": 0.14,
    "EUR": 0.13,
    "GBP": 0.11,
    "INR": 13.70,
    "AUD": 0.22,
    "CAD": 0.20,
    "JPY": 19.90,
    "CHF": 0.13
}

}
@app.route('/currency', methods=['GET'])
def get_exchange_rate():
    base = request.args.get('base','').upper()
    target = request.args.get('target','').upper()
    
    if not base or not target:
        return jsonify({
            "error": "Both 'Base' and 'Target' parameters are required"
        }),400
    if base not in EXCHANGE_RATES or target not in EXCHANGE_RATES:
        return jsonify({
            "error": "Invalid currency codes"
        }),400
    
    rate = EXCHANGE_RATES[base][target]
    return jsonify({
        "Base": base,
        "Target":target,
        "Rate":rate
    })

if __name__ =="__main__":
    app.run(debug=True)