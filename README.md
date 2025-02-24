# **Capstone-project-outcome-with-deliverable-project**

## **Project Overview**
This project is a **deliverable capstone project** that focuses on an **Advanced Search Engine & Recommendation System**. The system enhances **entity search** by retrieving detailed information from **Wikipedia** and recommending related entities using **clustering-based techniques**.

This project involved **extensive research**, including:

- **Manual vs. DBpedia-based Knowledge Graphs**
- **Embedding techniques (BERT, Word2Vec, etc.)**
- **Clustering methodologies for entity recommendations**

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
