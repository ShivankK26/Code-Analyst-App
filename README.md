# Code Review App ☕️

Welcome to the Code Review App! This app allows you to upload your Python (.py) files and receive suggestions for improvements using the GPT-3.5 model.

## How to Use

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

   ```
   git clone https://github.com/ShivankK26/Code-Analyst-App.git
   ```

2. **Install Dependencies**: Install the necessary dependencies by running the below command in your terminal.

   ```
   pip install -r requirements.txt
   ```

3. **Run the Application**: Execute the `app.py` file using Streamlit. Run `streamlit run app.py` in your terminal.

4. **Upload Your Python File**: Click on the button to upload your Python file (.py) that you want to get reviewed.

5. **Review Suggestions**: After uploading your file, our system will process it using the GPT-3.5 model and provide suggestions for improvements.

6. **Download Reviewed Code**: You can download the reviewed code file after receiving the suggestions.

## Dependencies

- `streamlit`: Web application framework for Python
- `dotenv`: Library for loading environment variables from a .env file
- `langchain`: Library for natural language processing tasks
- `openai`: Python client for OpenAI services (GPT-3.5 model)

## How it Works

The app uses the GPT-3.5 model from OpenAI to provide suggestions for improving Python code. It prompts you to upload your Python file, processes it using the GPT-3.5 model, and then displays the suggestions for improvements.
