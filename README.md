# AI-ML Driven Detection and Response System on Phishing Attacks

A web-based application that uses **Machine Learning** to detect and classify **phishing URLs** in real time.  
The system analyzes multiple URL-based features and predicts whether a website is **legitimate or phishing**, helping users make safer online decisions.

---

## 📖 Project Overview

Phishing attacks are one of the most common cybersecurity threats, targeting users by tricking them into visiting malicious websites.  
This project proposes an **AI-ML based phishing URL detection system** that leverages a **Gradient Boosting Classifier (GBC)** to accurately identify phishing URLs.

The system allows users to:
- Enter a URL
- Analyze its characteristics
- Instantly receive a **Safe / Unsafe** classification with confidence

This project was developed as a **B.Tech Final Year Project (2023–2024)** in **Computer Science & Engineering (Cyber Security)**.

---

## 🎯 Objectives

- Detect phishing URLs using machine learning techniques  
- Provide real-time URL safety evaluation  
- Minimize false positives and false negatives  
- Create a user-friendly web interface for easy access  
- Improve user awareness and protection against phishing attacks  

---

## 🧠 Machine Learning Model

- **Algorithm Used:** Gradient Boosting Classifier (GBC)
- **Type:** Supervised Learning (Binary Classification)
- **Output Classes:**  
  - Legitimate URL  
  - Phishing URL  

### Key Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

**Achieved Accuracy:** ~97%

---

## 🔍 Features Extracted from URLs

The system extracts **30 different features**, including:

- URL length  
- Presence of IP address  
- HTTPS usage  
- Domain age  
- Number of subdomains  
- Presence of special characters (@, //, -)  
- Redirections  
- Google indexing  
- Website traffic  
- PageRank  
- DNS records  
- iFrame redirection  
- Popup windows  
- Right-click disable detection  

These features help the model distinguish between legitimate and malicious URLs effectively.

---

## 🖥️ System Architecture

1. User enters a URL  
2. Feature extraction module analyzes the URL  
3. Extracted features are passed to the ML model  
4. Gradient Boosting Classifier predicts the result  
5. Output is displayed on the web interface  

---

## 🛠️ Technologies Used

### Programming & Frameworks
- Python  
- Flask  

### Frontend
- HTML  
- CSS  
- JavaScript  

### Machine Learning & Data Processing
- Scikit-learn  
- Pandas  
- NumPy  

### Additional Libraries & Tools
- BeautifulSoup (HTML parsing)
- Requests (HTTP requests)
- WHOIS API (Domain information)
- Google Search API

---

## 🌐 Web Application Features

- Real-time URL prediction  
- Confidence score for predictions  
- Simple and intuitive UI  
- Accessible through any web browser  
- Scalable and lightweight architecture  

---

## 📊 Results

- High classification accuracy (~97%)
- Strong performance across precision and recall metrics
- Reliable detection of both phishing and non-phishing URLs
- Effective real-world testing with diverse datasets

---

## ⚠️ Limitations

- Model performance depends on dataset quality  
- Possibility of false positives / false negatives  
- Requires continuous updates to handle evolving phishing techniques  
- Dependent on internet connectivity for external feature extraction  

---

## 🚀 Future Enhancements

- Integration of **Deep Learning models** (CNN / LSTM)
- Explainable AI (XAI) for better transparency
- Browser extension for live URL checking
- Email phishing detection
- Integration with enterprise security systems
- Automated threat intelligence updates

---

## 👩‍💻 Contributors

- **Shivani Dwivedi**  
- **Ayush Zode**

---

## 🎓 Academic Details

- **Degree:** B.Tech – Computer Science & Engineering (Cyber Security)  
- **Institute:** Shri Ramdeobaba College of Engineering & Management, Nagpur  
- **Guide:** Prof. Firdous Sadaf  
- **Academic Year:** 2023–2024  

---

## 📜 License

This project is developed for **academic purposes**.  
Feel free to use it for learning, research, and non-commercial use with proper attribution.

---



