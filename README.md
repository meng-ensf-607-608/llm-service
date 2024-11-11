# llm-service


## Running the application as a docker container (recommended)


1. **Install Docker Engine**:
   For instructions on how to install Docker Engine on your machine, see: https://docs.docker.com/engine/install/


2. **Build the image**:
    ```sh
    docker build -t llm-service .
    ```

3. **Create an '.env' file in the application root directory**

    ```
    ## gemini llm model version[Optional, if not specified 'gemini-1.5-flash' will be used]
    GOOGLE_LLM_MODEL=gemini-1.5-flash
    ## Gemini API key
    GOOGLE_API_KEY=
    APP_HOST=0.0.0.0
    ```
3. **Run the Application**:
    ```sh
    docker run -d --name llm-service-api -p 8080:8080 --env-file .env llm-service
    ```

## Running the application directly on your machine

1. **Ensure Pipenv is installed**
    
    If you don't have it on your machine, you can install it using:
    ```sh
        pip install pipenv
    ```


2. **Navigate to your project directory**

3. **Install dependencies**
    
    To install all the dependencies listed in the Pipfile, run:
    ```sh
        pipenv install --dev
    ```    

    This will create a virtual environment (if it doesn't already exist) and install the all therequired packages, including development dependencies (listed under [dev-packages] in the Pipfile).

4. **Sync with Pipfile.lock (optional)**
    If you want to ensure that the exact versions from the Pipfile.lock are installed, use:
    ```sh
        pipenv sync
    ```
    This is useful when you want to replicate an environment exactly as specified in the lock file

5. **Create an '.env' file in the application root directory**

    ```
        ## gemini llm model version[Optional, if not specified 'gemini-1.5-flash' will be used]
        GOOGLE_LLM_MODEL=gemini-1.5-flash
        ## Gemini API key
        GOOGLE_API_KEY=
    ```

6. **Run the application**
    ```sh
        python serve.py
    ```


## Invoking the api

Use a tool like Postman to invoke the model

```
Method: POST
```
```
url: http://127.0.0.1:8080/diagnose/invoke
```
```
request body example:
{
    "input": {
        "age": 23,
        "complaints": "headache backpain  neck strain",
        "gender": "male",
        "chronic_conditions": "migrain",
        "occupation": "construction worker"
    }
}
```
```
response example:
{
    "output": {
        "likely_causes": [
            {
                "cause": "Muscle Strain",
                "severity": 1,
                "symptoms": [
                    "Headache",
                    "Back pain",
                    "Neck strain",
                    "Muscle tenderness",
                    "Limited range of motion"
                ]
            },
            {
                "cause": "Migraine",
                "severity": 2,
                "symptoms": [
                    "Severe headache",
                    "Nausea",
                    "Vomiting",
                    "Sensitivity to light and sound",
                    "Visual disturbances"
                ]
            },
            {
                "cause": "Poor Posture",
                "severity": 3,
                "symptoms": [
                    "Headache",
                    "Back pain",
                    "Neck strain",
                    "Muscle tightness",
                    "Numbness or tingling in the arms or hands"
                ]
            },
            {
                "cause": "Dehydration",
                "severity": 4,
                "symptoms": [
                    "Headache",
                    "Fatigue",
                    "Dizziness",
                    "Muscle cramps"
                ]
            },
            {
                "cause": "Stress",
                "severity": 5,
                "symptoms": [
                    "Headache",
                    "Back pain",
                    "Neck strain",
                    "Muscle tension",
                    "Anxiety",
                    "Insomnia"
                ]
            }
        ],
        "lifestyle_changes": [
            "Maintain good posture while working",
            "Take regular breaks to stretch and move around",
            "Use proper lifting techniques",
            "Avoid prolonged sitting or standing",
            "Engage in regular exercise",
            "Get enough sleep",
            "Manage stress levels",
            "Practice relaxation techniques"
        ],
        "dietary_changes": [
            "Stay hydrated by drinking plenty of water",
            "Eat a balanced diet rich in fruits, vegetables, and whole grains",
            "Limit caffeine and alcohol intake",
            "Avoid processed foods and sugary drinks",
            "Consider taking a magnesium supplement"
        ]
    },
    "metadata": {
        "run_id": "7073f369-8b30-4a42-9d0d-a67dc47dc62f",
        "feedback_tokens": []
    }
}
```