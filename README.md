# EcoEye Online Bird Monitoring System

## Overview

**EcoEye** is an advanced **Online Bird Monitoring System** designed to track, identify, and monitor bird species in real-time through automated image recognition and sensor data. The system collects data from various remote locations, processes it using machine learning algorithms, and provides a comprehensive platform for bird conservationists, researchers, and nature enthusiasts to access up-to-date bird activity and population data.

By utilizing **computer vision**, **AI-based classification**, and **cloud computing**, EcoEye aims to promote biodiversity monitoring, wildlife protection, and environmental conservation efforts.

### Features:
- **Real-Time Bird Monitoring**: Monitors birds through live feeds from remote cameras and sensors.
- **Bird Identification**: Identifies bird species using AI-powered image classification models.
- **Automatic Data Collection**: Collects and stores bird observation data like sightings, species, and timestamps.
- **Cloud-Based Dashboard**: Provides users with a dashboard for visualizing bird sightings, species trends, and other relevant data.
- **Data Export**: Allows users to export collected bird sighting data for further research or analysis.
- **Environmentally Sustainable**: Promotes conservation by making bird data easily accessible to conservationists, researchers, and the public.

---

## Table of Contents

1. [Installation](#installation)
2. [Dataset](#dataset)
3. [System Overview](#system-overview)
4. [Technology Stack](#technology-stack)
5. [Usage](#usage)
6. [Evaluation](#evaluation)
7. [Contributions](#contributions)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)

---

## Installation

Follow the steps below to set up the **EcoEye Online Bird Monitoring System** locally:

### Prerequisites:
Ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package manager)

### Steps:
1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/EcoEye-Online-Bird-Monitoring-System.git
    cd EcoEye-Online-Bird-Monitoring-System
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

---

## Dataset

The system uses bird image datasets to identify species. The dataset may contain images of various bird species, recorded either by sensors or cameras installed in different ecological zones.

### Dataset Files:
- `bird_images/`: Directory containing bird images.
- `labels.csv`: File containing metadata about bird species, such as name, habitat, and other identification characteristics.

The dataset can be used for training the classification models and can be found through various open-source wildlife repositories, or you can contribute to expanding the dataset by uploading images and observations to the system.

---

## System Overview

The **EcoEye Online Bird Monitoring System** is built to:
- Capture real-time data from remote locations using cameras and sensors.
- Process captured images through AI models for bird species identification.
- Store bird sighting data (e.g., species, timestamps, locations) for analysis.
- Present the data in a user-friendly web interface/dashboard for conservationists and researchers.

The system follows these steps:

1. **Data Capture**: Cameras and sensors are set up in bird-watching zones.
2. **Bird Identification**: Captured images are processed by AI models to identify bird species.
3. **Cloud Storage**: Sightings and bird data are stored securely on the cloud.
4. **Web Dashboard**: Users can access a web interface to view and analyze bird sightings.

---

## Technology Stack

The system uses a variety of technologies, including:

- **Python** for backend development and machine learning model implementation.
- **TensorFlow / PyTorch** for training AI models for bird species identification.
- **Flask / Django** for the backend server.
- **React** for the frontend dashboard.
- **AWS** or **Google Cloud** for cloud data storage and processing.
- **OpenCV** for image processing.
- **SQLite / PostgreSQL** for data storage.

---

## Usage

Once the system is set up and running, you can use the following features:

### 1. Bird Species Identification

The system automatically classifies bird species in real-time using a pre-trained model:

```python
from bird_monitoring import BirdClassifier

# Initialize bird classifier
classifier = BirdClassifier()

# Classify bird from image
image_path = "path/to/bird_image.jpg"
species = classifier.predict(image_path)

print(f"The bird species is: {species}")
```
## Contributions

Contributions are highly encouraged! If you'd like to contribute to the **EcoEye-Online-Bird-Monitoring-System**, please follow these steps:

- Fork the repository.
- Create a new branch:  
  `git checkout -b feature-branch`
- Make your changes and commit them:  
  `git commit -m 'Add feature'`
- Push your changes to your fork:  
  `git push origin feature-branch`
- Submit a pull request.

We appreciate your contributions and will review your pull request as soon as possible!




Dataset Resource link: "https://azureloyalistcollege-my.sharepoint.com/personal/vishaldadabhaigir_loyalistcollege_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fvishaldadabhaigir%5Floyalistcollege%5Fcom%2FDocuments%2FBirds%5Fdata&view=0"
 
Data is collected from different platforms.

UI page Video: "https://azureloyalistcollege-my.sharepoint.com/:v:/g/personal/pulkitbatra_loyalistcollege_com/EXVuUt0k5IJPqYrYvjmj3d8BVGFpNgRBC__2UUA8Tjvgiw?e=ejFFCY&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D" 

UI pic: "https://drive.google.com/file/d/1l63hYu0EiY8niY5fnohQhDnGuqUFVEGi/view?usp=sharing"

How to create Virtual environment? and install packages and libraries: https://github.com/TechnoVishalGirase/Step_presentation_2/blob/main/13_3_2024/Commands_to_create_virtual_environment.txt

Model deployment and stress testing: https://github.com/TechnoVishalGirase/Step_presentation_2/blob/main/13_3_2024/Stress_testing.docx

**Contributors**
<hr> 
<a href="https://avatars.githubusercontent.com/u/67047845?s=400&u=71fd8132682e8d6822f8ea748904fe86020d6e36&v=4"><img src="https://avatars.githubusercontent.com/u/67047845?s=400&u=71fd8132682e8d6822f8ea748904fe86020d6e36&v=4" width="150px" height="150px" /></a>
</p>
 
[Pulkit Batra](https://github.com/batrapulkit)*                                                                                                                                                                                                                                                      
 <a href="https://github.com/batrapulkit"><img src="https://cdn.iconscout.com/icon/free/png-256/github-108-438008.png" width="32px" height="32px"></a> <a href="https://www.instagram.com/pulkit2001batra/"><img src="https://cdn.iconscout.com/icon/free/png-512/free-instagram-216-721958.png" width="32px" height="32px"></a> <a href="https://www.linkedin.com/in/pulkit-batra-14972a199/"><img src="https://i.ibb.co/Kx2GSrT/linkedin.png" width="32px" height="32px"></a><a href="https://www.facebook.com/pulkit.batra.14/"><img src="https://cdn.iconscout.com/icon/free/png-512/free-facebook-263-721950.png" width="32px" height="32px"></a>

<hr/>
<hr>
<hr>       
