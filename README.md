# AntiDrowsySystem 🚗💤

## Description 📝

The **AntiDrowsySystem** is an advanced Python-based system that uses **OpenCV**, **AI**, and **Machine Learning** to detect drowsiness by monitoring facial features like eyes and mouth. It uses pre-trained Haar cascade classifiers for detecting faces, eyes, and mouth, as well as a machine learning model to predict if the user is drowsy.

The system provides real-time monitoring and alerts to prevent drowsiness while driving or during other critical activities. The project uses a user-friendly GUI for easy interaction.

---

## Features 🌟

- **Real-Time Face Detection**: Utilizes Haar cascade classifiers to detect faces, eyes, and mouth. 👁️👄
- **Drowsiness Detection**: AI-based model to analyze eye and mouth states for detecting drowsiness. 🧠
- **Alert System**: Sounds an alarm or provides visual cues when drowsiness is detected. 🚨
- **Graphical User Interface (GUI)**: Simple, intuitive interface for interaction. 🖥️
- **Cross-Platform**: Developed using Python, works on both Windows and Linux systems. 🖥️🔄

---

## Technologies Used 🛠️

- **Python** 🐍
- **OpenCV** 📸
- **Classifiers** 🔍
- **Machine Learning** 🤖
- **GUI Framework** (for visualization and interaction) 🖥️

---

## Installation 🏗️

1. Clone the repository:
    ```bash
    git clone https://github.com/anmol8070/AntiDrowsySystem.git
    ```

2. Install the required libraries:
    ```bash
    pip install opencv-python
    pip install opencv
    pip install numpy
    pip install scikit-learn
    ```

3. Download the Haar cascade files and place them in the `haar cascade files/` directory:
    - `haarcascade_frontalface_alt.xml`
    - `haarcascade_lefteye_2splits.xml`
    - `haarcascade_righteye_2splits.xml`
    - `haarcascade_mcs_mouth.xml`

4. Ensure the `model.pkl` file is placed in the root directory of the project.

---

## How to Use 🛠️

1. Run the Python script:
    ```bash
    python AntiDrowsySystem.py
    ```

2. The GUI will open, and the system will start detecting your face, eyes, and mouth.

3. If the system detects drowsiness based on your facial features, an alert will be triggered. 🚨

---

## Files Overview 📂

- **`AntiDrowsySystem.py`**: Main Python script to run the system. Contains the logic for face, eye, and mouth detection, as well as drowsiness detection. 🔍
- **`model.pkl`**: Machine learning model for predicting drowsiness. 🤖
- **`haar cascade files/`**: Folder containing Haar cascade XML files for face, eye, and mouth detection. 🔐

---

## Contributing 🤝

Feel free to fork the repository and contribute by opening issues or pull requests. Contributions are always welcome! 🎉

---

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 📝

---

## Acknowledgments 👏

- OpenCV for computer vision tasks. 👁️
- The developers and researchers behind machine learning models used in drowsiness detection. 🤖
- The community for providing Haar cascade files for object detection. 🔬

