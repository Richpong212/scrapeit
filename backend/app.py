from flask import Flask, request, jsonify
from scraper import Scraper

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Welcome to the Flask Scraper API"}

@app.route("/scrape", methods=["POST"])
def scrape():
    try:
        # Parse input data
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        # Extract required parameters
        interest = data.get("interest")
        country = data.get("country")

        if not country:
            return jsonify({"error": "Country is required."}), 400
        if not interest:
            return jsonify({"error": "Interest is required."}), 400
        

        # Perform scraping
        scraper = Scraper(country,interest)
        result = scraper.google_search()

        # Return response
        return jsonify({
            "message": f"Scraping completed for {country} with interest {interest}.",
            "result": result
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
