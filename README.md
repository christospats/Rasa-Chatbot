# Rasa-Chatbot

## Description
This project was developed as part of an assignment for University of Macedonia. It is a chatbot designed to provide basic information regarding the issuance of a professional practice license for computer engineers. The information was sourced from the [mitos](https://mitos.gov.gr/index.php/ΔΔ:Άδεια_Εξάσκησης_Επαγγέλματος_Διπλωματούχου_Ναυπηγού_Μηχανολόγου_Μηχανικού) website.

## How to create your own interface in rasa

1. First, create an HTML file inside your Rasa project folder. Mine is the index.html.
2. If you don't want to start from scratch copy/ paste my file (index.html) inside your folder.

Let's have a look at my code:

**Style**

``` css
<style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #f0f0f0;
            gap: 20px;
        }
        header {
            width: 100%;
            background-color: #003375;
            color: white;
            padding-top: 15px;
            padding-bottom: 15px;
            text-align: center;
            font-size: 24px;
        }
        #chat-container {
            width: 100%;
            max-width: 1500px;
            background: white;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
        }
        #chat-box {
            height: 400px;
            overflow-y: scroll;
            padding: 20px;
            border-bottom: 1px solid #ddd;
        }
        #user-input {
            display: flex;
            padding: 10px;
        }
        #user-input input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        #user-input button {
            padding: 10px;
            border: none;
            background: #003375;
            color: white;
            cursor: pointer;
            border-radius: 4px;
            margin-left: 10px;
        }
    </style>
```
To change the color of the header, go to the header CSS block and change the background-color property. For the color of the "send" button, go to the #user-input button CSS block and change the background property. Of course, you can experiment with every CSS selector and block to create your ideal chatbot.

**HTML**
```html
<body>
    <!-- html code for the interface -->
    <header>Rasa Chatbot</header>
    <div id="chat-container">
        <div id="chat-box"></div>
        <div id="user-input">
            <input type="text" id="user-message" placeholder="Type a message..." />
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>
```
You can change the name of the header from 'Rasa Chatbot' to whatever you like, and the name of the button 'Send' to whatever you want. Feel free to add any other components you like to make it closer to your ideal chatbot.

**Javascript**
Let's check the js code and what you could change.

```javascript
// Append message
            function appendMessage(sender, message) {
                const messageElement = document.createElement('div');
                messageElement.innerHTML = `${sender}: ${message}`;
                messageElement.style.padding = '10px';
                messageElement.style.borderBottom = '1px solid #ddd';
                // Its an if condition (if sender = user then right else left) 
                messageElement.style.textAlign = sender === 'User' ? 'right' : 'left';
                messageElement.style.color = sender === 'User' ? '#003375' : '#333';
                chatBox.appendChild(messageElement);
                chatBox.scrollTop = chatBox.scrollHeight;
            }
```
The appendMessage function generates messages based on the sender. You can adjust padding, borderBottom, and color according to your preferences. I advise against altering anything else.

```javascript
// Create buttons for bot responses
            function createButtons(buttons) {
                buttons.forEach(button => {
                    const buttonElement = document.createElement('button');
                    buttonElement.textContent = button.title;
                    Object.assign(buttonElement.style, {
                        padding: '10px',
                        border: 'none',
                        background: '#003375',
                        color: 'white',
                        cursor: 'pointer',
                        borderRadius: '4px',
                        margin: '10px 0 0 10px'
                    });
                    buttonElement.addEventListener('click', () => handleButtonClick(button.title));
                    chatBox.appendChild(buttonElement);
                });
                chatBox.scrollTop = chatBox.scrollHeight;
            }
```
The createButtons function generates buttons if there are any. You can customize their style. I recommend avoiding unnecessary changes.

```javascript
 // Send request to bot
            async function sendRequest(message, isUserMessage = true) {
                if (isUserMessage) {
                    appendMessage('User', message);
                }
                userMessageInput.value = '';

                try {
                    const response = await fetch('http://localhost:5005/webhooks/rest/webhook', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ message })
                    });
                    const data = await response.json();

                    if (data && data.length > 0) {
                        const combinedMessage = data.map(msg => msg.text).join('<br>');
                        appendMessage('Bot', combinedMessage);

                        // Check for and create buttons
                        data.forEach(msg => {
                            if (msg.buttons && msg.buttons.length > 0) {
                                createButtons(msg.buttons);
                            }
                        });
                    }
                } catch (error) {
                    console.error('Error:', error);
                }
            }
```
The sendRequest function sends a POST request to http://localhost:5005/webhooks/rest/webhook, which is standard for everyone (unless you've modified the port). It should function correctly with most chatbots, so refrain from making unnecessary alterations.

```javascript
// Initial message on page load
            async function requestInitialMessage() {
                try {
                    const response = await fetch('http://localhost:5005/webhooks/rest/webhook', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ message: "/greet" })
                    });
                    const data = await response.json();

                    if (data && data.length > 0) {
                        const combinedMessage = data.map(msg => msg.text).join('<br>');
                        appendMessage('Bot', combinedMessage);

                        // Check for and create buttons if present
                        data.forEach(msg => {
                            if (msg.buttons && msg.buttons.length > 0) {
                                createButtons(msg.buttons);
                            }
                        });
                    }
                } catch (error) {
                    console.error('Error:', error);
                }
            }
```
requestInitialMessage is the function I use to initiate the chatbot's greeting to the user. Ensure to replace "/greet" with the desired intent to start the conversation, such as "/goodbye" or "/files".

The rest of the code should remain as is.

Final step: Go to your command prompt (cmd) and navigate to your Rasa directory. Run the following command:

```cmd
rasa run -m models --enable-api --cors "*"
```
Wait until you see the message "Rasa server is up and running". Then, double-click your HTML file to open it in your preferred browser. Your setup should be ready.

If your Rasa project includes custom actions, you'll need to run:
```cmd
rasa run actions
```
