# IoT Temperature Monitoring Project

## Overview

This project demonstrates an IoT solution for temperature monitoring in a hotel environment. It uses the MQTT protocol for communication and involves three main components:

1. **Publisher**: A Python script that simulates temperature readings and publishes them to an MQTT broker.
2. **Subscriber**: A Python script that subscribes to the MQTT topic, processes the temperature data, and saves it locally.
3. **Server**: A Flask-based HTTP server that exposes the latest temperature data through an API.




### 2. Set Up Python Environment

1. **Clone the Repository**
   - Clone the project repository (replace `<username>` and `<repository>` with actual values):
     ```bash
     git clone https://github.com/<username>/IoTProject.git
     ```
   - Navigate to the project directory:
     ```bash
     cd IoTProject
     ```

2. **Create a Virtual Environment**
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     ```bash
     .\venv\Scripts\activate
     ```

3. **Install Required Packages**
   - Install the necessary Python packages:
     ```bash
     pip install -r requirements.txt
     ```

## Configuration

1. **Publisher Script (`publisher.py`)**
   - Simulates temperature data and publishes it to the MQTT topic `hotel/temperature`.
   - Data is published every 60 seconds.

2. **Subscriber Script (`subscriber.py`)**
   - Subscribes to the `hotel/temperature` topic.
   - Saves temperature data to `temperature_data.txt`.
   - Raises an alarm if the temperature exceeds the threshold for 5 minutes.

3. **Server Script (`server.py`)**
   - A Flask server exposing the latest temperature data via an HTTP endpoint.
   - Accessible at `http://localhost:5000/latest_temperature`.

## Running the Project

1. **Start the Publisher Script**
   - In a Command Prompt window, navigate to the project directory and activate the virtual environment:
     ```bash
     cd C:\IoTProject
     .\venv\Scripts\activate
     ```
   - Run the publisher script:
     ```bash
     python publisher.py
     ```

2. **Start the Subscriber Script**
   - Open another Command Prompt window, navigate to the project directory, and activate the virtual environment:
     ```bash
     cd C:\IoTProject
     .\venv\Scripts\activate
     ```
   - Run the subscriber script:
     ```bash
     python subscriber.py
     ```

3. **Start the Server Script**
   - Open yet another Command Prompt window, navigate to the project directory, and activate the virtual environment:
     ```bash
     cd C:\IoTProject
     .\venv\Scripts\activate
     ```
   - Run the server script:
     ```bash
     python server.py
     ```

## Accessing the Data

- **Latest Temperature Data**:
  - Open a web browser and go to:
    ```bash
    http://localhost:5000/latest_temperature
    ```

