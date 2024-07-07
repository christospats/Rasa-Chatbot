# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# class CheckEnglishInputAction(Action):
#     def name(self) -> Text:
#         return "action_check_english_input"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         # Get the user input
#         user_input = tracker.latest_message.get("text", "")

#         # Check if the input contains English characters
#         if any(char.isalpha() and char.lower() >= 'a' and char.lower() <= 'z' for char in user_input):
#             response = "True"

#         print(response)
#         # Send the response back to the user
#         dispatcher.utter_message(text=response)
        

#         return []
    
# class CheckEnglishInputActionBoolean(Action):

#     def name(self) -> Text:
#         return "action_check_english_input_boolean"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         # Get the user input
#         user_input = tracker.latest_message.get("text", "")

#         # Check if the input contains English characters
#         contains_english = any(char.isalpha() and char.lower() >= 'a' and char.lower() <= 'z' for char in user_input)

#         print(contains_english)
#         # Return True if input contains English characters, False otherwise
#         return [SlotSet("has_english", contains_english)]
    
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import ActionExecuted
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

# class CustomActionReturnAction(Action):
#     def name(self) -> Text:
#         return "custom_action_return_action"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         # Extract the intent names
#         intent_names = domain.get("intents", [])


#         # Check if the intent 'your_intent_name' is present in the latest user message
#         print(tracker.latest_message['intent'].get('name'))
#         print(intent_names)
#         for intent in intent_names:
#             if tracker.latest_message['intent'].get('name') != intent:
#                 dispatcher.utter_message(text="Δεν κατάλαβα την ερώτηση. Παρακαλώ επαναδιατυπώστε. Παρακαλώ μόνο στα Ελληνικά")
#                 return []
#             else:
#                 return[]
        
        
# costs = {
#     "τ.ε.ε": "20€",
#     "συνδρομη": "20€",
#     "παραβολο": "29.35€",
#     "συνολικο": "107,01€",
#     "χαρτοσημο": "1.66€",
#     "τελη": "36€",
#     "κοστος":"<br>Η συνολική διαδικασία θα κοστισεί 107,01.<br>Αναλυτικά τα κόστοι είναι:<br>Πληρωμή δικαιώματος εγγραφής μέλους Τ.Ε.Ε: 20€<br>Παράβολο συμμετοχής για τις εξετάσεις €29,35 (€9,78 για κάθε μία από τις 3 υποχρεωτικές ενότητες επιλογής του υποψηφίου): 29.35€<br>Ετήσια συνδρομή μέλους στο Τ.Ε.Ε: 20€<br>Χαρτόσημο παραβόλου 2,4% επί του ποσού € 69,35: 1.66€<br>Τέλος Χαρτοσήμου Άδειας Άσκησης Επαγγέλματος: 36€",
#     "κοστοι":"<br>Η συνολική διαδικασία θα κοστισεί 107,01.<br>Αναλυτικά τα κόστοι είναι:<br>Πληρωμή δικαιώματος εγγραφής μέλους Τ.Ε.Ε: 20€<br>Παράβολο συμμετοχής για τις εξετάσεις €29,35 (€9,78 για κάθε μία από τις 3 υποχρεωτικές ενότητες επιλογής του υποψηφίου): 29.35€<br>Ετήσια συνδρομή μέλους στο Τ.Ε.Ε: 20€<br>Χαρτόσημο παραβόλου 2,4% επί του ποσού € 69,35: 1.66€<br>Τέλος Χαρτοσήμου Άδειας Άσκησης Επαγγέλματος: 36€"
# }

# class ActionFindAndShowCost(Action):

#     def name(self) -> Text:
#         return "action_find_and_show_cost"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         cost = tracker.get_slot("cost")
#         print(cost)
#         cost_out = costs.get(cost.lower())

#         if cost_out is None:
#             output = "Δεν μπορουσα να βρω κοστος για {}".format(cost)
#         else:
#             if cost == "κοστος" or cost == "κοστοι":
#                 output = "Συνολικο κόστος υπηρεσιών:<br>{}".format(cost_out)
#             else:
#                 output = "Το κόστος για {} είναι {}".format(cost, cost_out)

#         dispatcher.utter_message(text=output)

#         return []


files = {
    "αντιγραφα": "Αντίγραφο τίτλου σπουδών αλλοδαπής ή ημεδαπής σχολής<br>Αντιγραφό αναλυτικής βαθμολογίας<br>Αντιγραφό της διπλοματικής εργασίας",
    "δηλωσεις" : "Υπεύθυνη Δήλωση του ενδιαφερόμενου στην οποία δηλώνει ότι: <br>α) δεν έχει τεθεί σε δικαστική συμπαράσταση,<br>β) δεν έχει καταδικαστεί αμετάκλητα για κακούργημα και δεν εκτίει ποινή ή ότι έχει καταδικαστεί και εκτίει ποινή για διάστημα «από … έως ...»,<br>γ) δεν είναι δημόσιος υπάλληλος ή είναι δημόσιος υπάλληλος και ασκεί ιδιωτικό έργο<br>δ) η διπλωματική εργασία και η περίληψή της έχουν εκπονηθεί από τον ίδιο.",
    "φωτοτυπιες": "Φωτοτυπία της αστυνομικής ταυτότητας ή Στρατιωτικής ταυτότητα ή διαβατήριου.",
    "φωτογραφιες": " Δύο (2) φωτογραφίες, αυστηρώς στις διαστάσεις της αστυνομικής ταυτότητας σε ματ χαρτί και στην πίσω όψη να αναγράφεται το ονοματεπώνυμό του ενδιαφερόμενου ή Υποβολή ψηφιακής φωτογραφίας προσώπου σε μορφή αρχείου jpeg τύπου αστυνομικής ταυτότητας.",
    "αιτησεις" : "Αίτηση Διάθεσης Δημοσιοποίησης Δεδομένων Προσωπικού Χαρακτήρα του ενδιαφερόμενου<br>Αίτηση «εγγραφής για τις δωρεάν υπηρεσίες του Τ.Ε.Ε. (My ΤΕΕ)». Απο site: https://web.tee.gr/exams/e-entypa/",
    "τιτλο σπουδων": "Πράξη ισοτιμίας τίτλου σπουδών της αλλοδαπής και αντιστοιχίας εκδοθείσα από τις αρμόδιες υπηρεσίες αναγνώρισης από το Διεπιστημονικό Οργανισμό Αναγνώρισης Τίτλων Ακαδημαϊκών και Πληροφόρησης (Δ.Ο.Α.Τ.Α.Π.), η οποία δύναται να αναζητηθεί και υπηρεσιακά.Αποτελεί δικαιολογιτικό με προϋπόθεση."
}


class ActionFindAndShowFile(Action):

    def name(self) -> Text:
        return "action_find_and_show_file"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        file = tracker.get_slot("file")
        print(file)
        files_out = files.get(file.lower())

        if files_out is None:
            output = "Δεν μπορουσα να βρω καποιο συγκεκριμένο δικαιολογητικό που να χρειάζεται {}".format(file)
        else:
            output = "θα χρειαστείτε:<br>{}".format(files_out)

        dispatcher.utter_message(text=output)

        return []
    
