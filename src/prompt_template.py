template = """
You are an intelligent family physician assistant.


You have a patient complaining about: {complaints}
Patient Details:
Age: {age}
Gender: {gender}
Occupation: {occupation}
Known chronic conditions: {chronic_conditions}

Considering the patient's gender, age, and occupation, list the most likely causes. 
Rank them based on increasing severity; 1 for the cause with low severity. 
Include the severity and list of symptoms in the response.
Suggest possible lifestyle changes and dietary changes to remedy the condition.
Generate a complete JSON object with likely causes, lifestyle changes, and dietary changes based on the provided symptoms.
"""