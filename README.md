# Sports GPT Assistant

A web application that uses OpenAI's GPT to answer sports-related questions.

## Setup

1. Clone the repository
2. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
3. Install the required Python packages:
   ```
   pip install flask flask-cors requests python-dotenv
   ```
4. Run the Flask server:
   ```
   python app.py
   ```
5. Open your browser and go to `http://localhost:5000`

## Security Note

Never commit your `.env` file to version control. The `.gitignore` file is already set up to prevent this.
