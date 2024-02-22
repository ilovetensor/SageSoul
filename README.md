# SageSoul 🍃

SageSoul is a groundbreaking project designed to support Ayurvedic practitioners in their journey, providing an extensive repository of knowledge, formulations, and guidance at their fingertips.

In the realm of modern medicine, there are abundant tools and resources, but Ayurveda lacks rich sources. Recognizing this gap, SageSoul aims to bridge it by introducing innovative software. The goal is to enhance the accessibility of Ayurveda, making diagnostics and prescription processes more straightforward.

In Ayurveda, prescribing medicines poses a unique challenge, as each individual requires a personalized set of medications based on their body composition. SageSoul addresses this challenge by leveraging technology and data to streamline the diagnostic and prescription processes.

## How it Works? 🪵

![SageSoul Image](https://github.com/ilovetensor/SageSoul/blob/f0f44d214d74ace3b4abd2d3198e4dcb85353450/Untitled.jpg)

- The project compiles essential data from various books and resources to create a comprehensive dictionary. This dictionary correlates symptoms with diseases and medicines, facilitating simultaneous diagnostics and prescription.

- Machine learning models are trained on this data to analyze a constellation of symptoms and predict the best match for effective treatment.

## Two Approaches 🔨

To tackle this challenge, SageSoul adopts two distinct approaches, each addressing specific challenges.

### 1. Similarity Search 🔎

- This approach utilizes the **Facebook AI Similarity Search** tool.
- Texts are extracted from books and segmented into paragraphs.
- These paragraphs are then converted into vectors.
- When a user submits a query, it is transformed into a vector.
- The system matches the query vector with the nearest vector in the paragraph space, presenting the top 5 results directly from the book.

### 2. ML Model 🪷

- The dataset is created by scraping Ayurveda repositories, capturing information about common diseases and symptoms.
- This data is used to train a machine learning model, which is then deployed on the website.
- Users input their symptoms, and the model predicts suitable medicines based on the trained information.

## Conclusion 🏁

- Developing an Ayurvedic assistant is a formidable challenge, but with ongoing research, it has the potential to revolutionize how Ayurveda is integrated into our lives.
- The current data availability is limited, and efforts should be directed towards enriching it.
- The majority of Ayurvedic texts are in Sanskrit; hence, translating more books into English would enhance accessibility.
