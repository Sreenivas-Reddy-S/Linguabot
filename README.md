# 🌟 **Bedrock Chatbot with Streamlit** 🌟

Hey there! 🤖💬 Want to chat with an AI powered by Amazon's **Bedrock** and serve it up with a smooth **Streamlit** interface? Well, you’re in the right place! This repo brings together the power of cutting-edge AI with an easy-to-use web interface. Whether you're asking about **New York medical colleges** 🏥 or curious about **Spanish** phrases 🇪🇸, this chatbot's got your back.

## 🛠️ **Tech Stack**

This project is built on:
- **Streamlit**: Easy, beautiful web apps for data science and machine learning.
- **Amazon Bedrock**: Access state-of-the-art AI models (like **Claude v2** from Anthropic) via AWS.
- **Langchain**: The power of language model chains, made easy.
- **Boto3**: For interacting with AWS services.

## 🚀 **Getting Started**

### Prerequisites

Before we start, make sure you have these installed:

1. **AWS CLI** & **AWS Account**: You'll need an AWS account with **Bedrock** access. If you don’t have one, hit up [AWS](https://aws.amazon.com/) and get started.
2. **Python 3.x**: Python's gotta be installed, duh.
3. **Streamlit**: The platform we use for creating the UI of our chatbot.
4. **Langchain, Boto3**: For linking up with the AI models.

### 🧑‍💻 **Setting up the Environment**

- Clone the repo:git clone https://github.com/Sreenivas-Reddy-S/Linguabot.git
- Install the dependencies: pip install -r requirements.txt
- Set up your **AWS profile**:
    - Make sure your **AWS CLI** is set up and the profile is configured with the necessary permissions for **Bedrock** access.
    - You can check if it's working by running: aws sts get-caller-identity
- 🛠️ **Configure `AWS_PROFILE`** in your `App.py` file (or set the environment variable globally in your terminal).
    - os.environ["AWS_PROFILE"] = "bedrock"  # Your AWS profile name
  

### 🎧 **Running the Chatbot**

1. First, run the **Streamlit** app: streamlit run streamlit.py
2. Open your browser and go to **http://localhost:8501**.
3. You’ll see a super chill interface where you can:
    - Choose **language** (English or Spanish, as of now).
    - Ask your **Question**.
    - Get an AI-powered response based on the Bedrock model.

### 🤖 **How It Works**

- You can ask anything, and the bot is ready to give you the goods.
- The bot uses **Bedrock’s Claude v2 model** to process your question and deliver a response.
- On the backend, **Langchain** makes it easy to tie the model and data together with custom prompts.
  
### 🧠 **Customizing It**

Want to tweak the model or add more languages? No problem! 🙌

- **Change the model**: If you want to try out another AI model (like **Haiku** or **Opus**), just swap out the model ID in the `App.py` file: modelID = "anthropic.claude-v2"  # Change to another model ID if needed

- **Add more languages**: Simply add more options in the Streamlit sidebar and modify the prompt in `App.py` to handle the new language.

### ⚙️ **API Integration**

This chatbot is powered by AWS Bedrock, which means you can connect to it via an API endpoint. The backend code uses **Langchain** and **Boto3** to interact with Bedrock's **Claude v2** model. All the magic happens in **`App.py`** where it builds the prompt dynamically based on the user's question and language.

#### API Request:

json:
{
  "inputs": "Your question here",
  "parameters": {
    "max_length": 100,
    "min_length": 30
  }
}

- URL: url

Headers:
- Authorization: Bearer YOUR_ACCESS_TOKEN
- Content-Type: application/json

💡 Why Bedrock + Streamlit?
- Super Scalable: AWS Bedrock models are designed to handle large-scale requests.
- Easy-to-Use Interface: Streamlit makes it super easy to spin up an interface for your chatbot in minutes.
- High Performance: With Claude v2 and Langchain working together, the response time is rapid, and the answers are on point.
- Modular: Want to swap out models or APIs? It's all flexible!

🔗 Resources:
- DeepLearning.Ai
- Google

Big thanks! 🙌 
Stay lit. Stay awesome.
