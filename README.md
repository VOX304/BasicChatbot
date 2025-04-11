# BasicChatbot

# 🐾 Pet Store AI Assistant
Welcome to the Pet Store AI Assistant — an intelligent chatbot built with Google Gemini to enhance your pet store experience! Whether you're a pet owner looking for advice or a store manager needing help with order handling, this assistant is here to help.

## 🌟 Features
💬 Natural conversation powered by Google Gemini

📦 Ask about products, make orders, or check stock

🐶 Get pet care recommendations and tips

🛠️ Easy setup with environment variables and Chainlit UI

## 🚀 How to Use
1. Clone the repository
bash
```
git clone https://github.com/yourusername/petstore-assistant.git
cd petstore-assistant
```

2. Set up your environment
Create a .env file in the root directory with your Gemini API Key:
```GEMINI_API_KEY=your_gemini_api_key_here```

3. Install dependencies
Make sure you have Python 3.8+ installed.
```pip install -r requirements.txt```

4. Run the chatbot

```chainlit run app.py```
This will launch a local chat interface where you can interact with the assistant in your browser.

## 💡 Use Cases
Here are some ways to use the Pet Store AI Assistant:

🐕 For Pet Owners
“What kind of food should I give my 3-month-old puppy?”

“How often should I groom a Persian cat?”

“Can you recommend some toys for a hyperactive dog?”

## 🛍️ For Store Staff or Managers
“Place an order for 10 bags of Royal Canin dog food.”

“Check if we have parrot cages in stock.”

“Summarize customer queries from today.”

## 📦 Project Structure
bash
Copy
Edit
petstore-assistant/
├── app.py                # Main entry point
├── .env                  # Environment variables
├── requirements.txt      # Python dependencies
└── src/
    └── prompt.py         # Contains system instructions for the chatbot
## 🧠 Powered By
Chainlit

Google Generative AI (Gemini)

Python Dotenv

## 📬 Feedback & Contributions
Feel free to open issues or pull requests to improve the assistant!
Let’s build a smarter pet care experience together. 🐾