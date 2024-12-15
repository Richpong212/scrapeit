# ScrapIt - A Web Scraping Tool

ScrapIt is an advanced, human-like scraping tool built using Playwright for backend operations and Vue.js for the frontend. It is designed to extract specific data such as emails, phone numbers, and source links from search results while mimicking human behavior to avoid detection.

---

## Features

1. **Human-Like Behavior**:
   - Introduces random delays between actions to simulate real user interaction.
2. **ReCAPTCHA Handling**:
   - Detects and allows manual resolution of Google reCAPTCHA challenges.
3. **Data Extraction**:
   - Retrieves valid email addresses, phone numbers, and associated links from Google search results.
4. **Pagination Support**:
   - Scrapes data across multiple pages of search results.
5. **Frontend Integration**:
   - Vue.js provides an intuitive and dynamic user interface for triggering scrapes and viewing results.

---

## Installation

### Prerequisites

- Python 3.7+
- Node.js and npm
- Playwright installed globally

### Backend Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/Scrapit.git
   cd ScrapIt/backend
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt --break-system-packages
   ```

3. Install Playwright dependencies:

   ```bash
   playwright install
   ```

4. Run the backend server:
   ```bash
   python3 app.py
   ```

---

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd ../frontend
   ```

2. Create a new Vue.js project with TypeScript:

   ```bash
   npm init vue@latest
   ```

3. Install dependencies:

   ```bash
   npm install
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

---

## Usage

1. Start the backend and frontend servers.
2. Access the frontend UI at `http://localhost:8080`.
3. Provide inputs such as `Interest` and `Country` for your search query.
4. Submit the query to start scraping.
5. View the extracted data, including:
   - Names
   - Valid email addresses
   - Phone numbers
   - Source links

---

## API Endpoints

### **POST /scrape**

**Request**:

- `Content-Type`: `application/json`
- Body:
  ```json
  {
    "interest": "marketing manager",
    "country": "USA"
  }
  ```

**Response**:

- Success (200):
  ```json
  {
    "message": "Scraping completed for USA with interest marketing manager.",
    "result": [
      {
        "name": "John Doe - Marketing Manager",
        "emails": ["john.doe@gmail.com"],
        "phone_numbers": ["+1234567890"],
        "source_link": "https://example.com"
      }
    ]
  }
  ```
- Error (400/500):
  ```json
  {
    "error": "Country is required."
  }
  ```

---

## Backend Code Structure

- **`app.py`**: Flask API for handling scraping requests.
- **`scraper.py`**: Contains the `Scraper` class for managing scraping logic.
- **`utils.py`**: Utility module for Playwright setup.

### Key Backend Features

1. **Playwright Integration**:
   - Setup with custom user-agent to mimic human browsing.
2. **Regex Validations**:
   - Extract and validate emails and phone numbers using refined regex patterns.
3. **ReCAPTCHA Detection**:
   - Prompts for manual resolution when encountering Google reCAPTCHA.

---

## Frontend Code Structure

The frontend is developed with Vue.js and TypeScript, providing an easy-to-use interface.

1. **Home Page**:
   - Displays a form for inputting search parameters.
2. **Results Page**:
   - Dynamically shows extracted data in a clean and organized layout.

---

## Advanced Functionalities

1. **Human-Like Behavior**:
   - Randomized delays simulate real user interaction during scraping.
2. **Pagination Handling**:
   - Automatically navigates through multiple pages of Google search results.
3. **Duplicate Filtering**:
   - Ensures unique entries for emails and phone numbers.

---

## Example Search Query

A sample query targeting Gmail and Yahoo users in the marketing field:

```bash
"marketing manager" intext:"@gmail.com" OR intext:"@yahoo.com" intext:"+1" "USA"
```

---

## Limitations

1. **ReCAPTCHA Handling**:
   - Currently requires manual intervention to solve reCAPTCHA challenges.
2. **Rate Limiting**:
   - Heavy usage may trigger rate limiting from Google.
3. **Dynamic Content**:
   - Fully AJAX-based sites may not yield accurate results.

---

## Future Enhancements

1. Automate solving reCAPTCHA using external services like `2Captcha`.
2. Add support for proxy rotation to avoid IP blocking.
3. Enhance the UI with real-time scraping status updates.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
