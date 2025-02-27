# **Capstone-project-outcome-with-deliverable-project**

## **Project Overview**
This project is a **deliverable capstone project** that focuses on an **Advanced Search Engine & Recommendation System**. The system enhances **entity search** by retrieving detailed information from **Wikipedia** and recommending related entities using **clustering-based techniques**.

This project involved **extensive research**, including:

- **Manual vs. DBpedia-based Knowledge Graphs**
- **Embedding techniques (BERT, Word2Vec, etc.)**
- **Clustering methodologies for entity recommendations**
![image](https://github.com/user-attachments/assets/b9f24bb0-a5ee-4743-9ab7-662ae2c358cf)

---

## **Project Components**

### **1. `final-query-kg-bert-cluster-w2vec-cluster (1).ipynb`**
- **Manual Knowledge Graph construction** with predefined relationships.
- **Entity embedding generation** using **BERT** and **Word2Vec**.
- **Clustering of entities** based on similarity.

### **2. `final-query-kg-bert-cluster-w2vec-cluster.ipynb`**
- **DBpedia-based Knowledge Graph analysis**.
- **Extracts structured entity information** using **SPARQL queries**.
- **Generates embeddings** and applies clustering techniques.

### **3. `capstone-scientist-player-actor.ipynb`**
- **Final integration of the Advanced Search Engine & Recommendation System**.
- **Processes and stores clustered entities** in `clusters.json` for use in the application.

### **4. `streamlit_app.py`**
A **Streamlit-based interactive application** that:
- **Searches for entities** and retrieves **Wikipedia data** (summary & images).
- **Finds related entities from the same cluster** and displays them with images & descriptions.

---

## **Research Contributions & Future Work**
- **Comparative analysis of manual vs. DBpedia-based KG.**
- **Clustering evaluation for better recommendations.**
- **Future improvements:** Expanding the KG, refining embeddings, and integrating real-time knowledge updates.

This project is a **practical application of advanced search and recommendation techniques**, demonstrating deep research in **Knowledge Graphs, NLP, and AI-driven search**. 🚀

## **Output images of the streamlit project:**
![image](https://github.com/user-attachments/assets/276e56bf-c39f-4e32-8354-30e39b475329)
![image](https://github.com/user-attachments/assets/4fd754a4-6095-45e6-a3ab-2eb029220c72)
![image](https://github.com/user-attachments/assets/7d1a2fd5-32a5-4745-9bcc-e52adc4e5ab9)
![image](https://github.com/user-attachments/assets/a9f96e01-7647-4e21-bb3d-79322cb0024b)

# Advanced Search Engine with Clustering-based Recommendation System

## Overview
This project is an **Advanced Search Engine** that integrates **Clustering-based Recommendations** to provide detailed information about specific entities and suggest related entities from the same cluster. It is designed to enhance information retrieval by grouping entities into clusters based on criteria such as profession, field of work, or other similarities.

## Features
1. **Entity Search**: Users can search for specific entities (e.g., Albert Einstein, Lionel Messi, Chanchal Chowdhury) to retrieve detailed information about them.
2. **Clustering-based Recommendations**: The system groups entities into clusters and recommends related entities from the same cluster when a user searches for a specific entity.
3. **User-Friendly Interface**: The system prompts users to enter an entity name to initiate a search, making it easy to use.
4. **Example Clusters**:
   - **Cluster 1**: Bangladeshi actors (e.g., Chanchal Chowdhury, Zahid Hasan, K.M. Mosharaf Hossain).
   - **Cluster 2**: Famous footballers (e.g., Lionel Messi, Pelé, Neymar, Cristiano Ronaldo).
   - **Cluster 3**: Renowned scientists and thinkers (e.g., Albert Einstein, Isaac Newton, Charles Darwin, Nikola Tesla).

## How to Use
1. **Search for an Entity**:
   - Enter the name of the entity you want to search for (e.g., `Albert_Einstein`, `Lionel Messi`, or `Chanchal Chowdhury`).
   - The system will display detailed information about the entity.

2. **View Recommendations**:
   - After displaying the details of the searched entity, the system will recommend related entities from the same cluster.
   - For example, if you search for `Albert Einstein`, the system may recommend `Isaac Newton`, `Charles Darwin`, and `Nikola Tesla`.

3. **Explore Clusters**:
   - You can explore different clusters by searching for entities within specific domains (e.g., actors, footballers, scientists).

## Example Queries
- Search for `Lionel Messi` to get details about him and recommendations like `Pelé`, `Neymar`, and `Cristiano Ronaldo`.
- Search for `Chanchal Chowdhury` to get details about him and recommendations like `Zahid Hasan` and `K.M. Mosharaf Hossain`.

## Purpose
The project aims to enhance information retrieval by providing detailed information about specific entities and suggesting related entities. This can be useful for research, exploration, or discovering similar figures or topics.


### **Copyright (c) 2025 PRINOM MOJUMDER. Email: prinommojumder19@gmail.com**


