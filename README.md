# BlueBox - AI-Powered Cold Calling Virtual Assistant

BlueBox is an AI-powered virtual assistant designed to handle customer interactions through cold calling. It automates customer queries, processes orders, collects feedback, and much more, all through phone calls. The system integrates advanced AI and telecommunication tools to streamline business-customer communication.

## Features

- Automated cold calling
- Real-time customer query handling
- Speech-to-text conversion for seamless processing
- Order processing and confirmation via phone calls
- Collecting and storing customer feedback
- Easy integration with existing CRM systems

## Tools and Technologies Used

- **[Groq](https://groq.com/)**: AI acceleration for high-speed inference and processing of large-scale models.
- **[Deepgram](https://deepgram.com/)**: Speech-to-text API used for transcribing customer conversations into text for further processing.
- **[Twilio](https://twilio.com/)**: Handles all phone-related operations such as initiating and managing phone calls.
- **[Flask](https://flask.palletsprojects.com/)**: Python micro-framework for backend development and API integration.
  
## How It Works

1. **Customer Calls**: Twilio is used to initiate outbound calls to customers.
2. **Speech Recognition**: Deepgram transcribes customer speech into text.
3. **AI-Powered Query Handling**: The text is processed by an AI model (leveraging Groq for acceleration), which determines the appropriate response based on customer input.
4. **Order Processing**: If the customer wishes to place an order, the system guides them through the steps and stores the order in the database.
5. **Feedback Collection**: At the end of the call, customers can provide feedback, which is collected and analyzed for business insights.

## Getting Started

### Prerequisites

- Python 3.11+
- Flask
- Groq SDK
- Twilio API account
- Deepgram API account

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/BlueBox.git
```
2.Navigate to the project directory:
 ```bash
cd BlueBox
```


3.Install the dependencies:
 ```bash
pip install -r requirements.txt
```


4.Set up your environment variables for Twilio and Deepgram:
 ```bash
export TWILIO_ACCOUNT_SID=your_twilio_sid
export TWILIO_AUTH_TOKEN=your_twilio_auth_token
export DEEPGRAM_API_KEY=your_deepgram_api_key
```


5.Run the flask application:
 ```bash
flask run
```

