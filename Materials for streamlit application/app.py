import streamlit as st
import numpy as np
import json
import requests
import wikipediaapi

# Wikipedia API Setup with a user agent
user_agent = "MyEntitySearchApp/1.0 (contact@mydomain.com)"  # Replace with your details
wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language="en")

def get_wikipedia_info(entity_name):
    """Fetch Wikipedia summary & image for the given entity."""
    page = wiki.page(entity_name.replace("_", " "))  # Convert DBpedia format to Wikipedia
    if not page.exists():
        return None, None

    summary = page.summary[:500]  # First 500 characters
    image_url = get_wikipedia_image(entity_name)

    return summary, image_url

def get_wikipedia_image(entity_name):
    """Fetch the first image from Wikipedia using two API methods."""
    # First try: Wikipedia Media API
    api_url = f"https://en.wikipedia.org/api/rest_v1/page/media-list/{entity_name.replace(' ', '_')}"
    response = requests.get(api_url).json()

    if "items" in response and response["items"]:
        for item in response["items"]:
            if "original" in item:
                return item["original"]["source"]  # First image found

    # Second try: Wikipedia Page Metadata API (sometimes more reliable)
    api_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{entity_name.replace(' ', '_')}"
    response = requests.get(api_url).json()
    
    if "thumbnail" in response and "source" in response["thumbnail"]:
        return response["thumbnail"]["source"]  # Return the thumbnail image

    return None  # No image found

# Load clustering results
@st.cache_data
def load_clusters():
    with open("clusters.json", "r") as f:
        return json.load(f)  # Example: {'Cluster_1': ['Albert_Einstein', 'Isaac_Newton'], ...}

clusters = load_clusters()

# Streamlit UI
st.title("🔍 Advanced Search Engine & Clustering based Recommendation system.")
st.write("Search for an entity to find its details and related entities from the same cluster.")

# Search Box
search_query = st.text_input("Enter an entity name (e.g., Albert_Einstein)", "")

if search_query:
    search_query = search_query.replace(" ", "_")  # Convert to DBpedia format

    # Find the entity's cluster
    entity_cluster = None
    for cluster, entities in clusters.items():
        if search_query in entities:
            entity_cluster = cluster
            break

    if entity_cluster:
        # Display entity details
        st.subheader(f"📌 {search_query.replace('_', ' ')}")
        summary, image_url = get_wikipedia_info(search_query)

        if image_url:
            st.image(image_url, width=300)
        if summary:
            st.write(summary)

        # Show other entities in the same cluster
        st.subheader(f"📚 Recommended Entities or People from {entity_cluster}")
        for entity in clusters[entity_cluster]:
            if entity != search_query:
                summary, image_url = get_wikipedia_info(entity)
                with st.container():
                    col1, col2 = st.columns([1, 3])
                    if image_url:
                        col1.image(image_url, width=100)
                    col2.write(f"**{entity.replace('_', ' ')}**")
                    col2.write(summary[:200] + "...")  # Short preview

    else:
        st.error("Entity not found in clusters. Try another name.")
