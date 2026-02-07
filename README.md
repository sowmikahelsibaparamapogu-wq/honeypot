# Honeypot Scam Detection

A FastAPI-based application that analyzes messages for potential scam-related words and provides a response indicating whether the message looks safe or suspicious.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/honeypot.git
    cd honeypot
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application, use the following command:

```bash
uvicorn main:app --reload
