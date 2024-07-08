# Rasa-Chatbot

## Description
This project was developed as part of an assignment for the University of Macedonia. It is a chatbot designed to provide basic information regarding the issuance of a professional practice license for computer engineers. The information was sourced from the [mitos](https://mitos.gov.gr/index.php/ΔΔ:Άδεια_Εξάσκησης_Επαγγέλματος_Διπλωματούχου_Ναυπηγού_Μηχανολόγου_Μηχανικού) website.

## How to create your own interface in rasa

1. First, create an HTML file inside your Rasa project folder. Mine is the index.html.
2. If you don't want to start from scratch copy/ paste my file (index.html) inside your folder.

Let's have a look at my code:
**Style**

``` html
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
