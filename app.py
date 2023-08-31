import streamlit as st
import pandas as pd

# Create data storage for ads and requests
ads_data = [
    {
        "Title": "Beautiful Villa for Sale",
        "Description": "Spacious 4-bedroom villa with a garden and pool.",
        "Type": "Sell",
        "Price": 500000,
        "Image": "villa.jpg",
        "Contact": "seller@example.com"
    },
    {
        "Title": "Cozy Apartment for Rent",
        "Description": "2-bedroom apartment in the city center. Available for rent.",
        "Type": "Rent",
        "Price": 1500,
        "Image": "villa.jpg",
        "Contact": "landlord@example.com"
    }
]
requests_data = []

# Set up the menu bar
st.sidebar.title("Menu")
menu_selection = st.sidebar.radio("Select a Service", ["Housing", "Other Services"])

# Depending on the menu selection, display the appropriate content
if menu_selection == "Housing":
    st.title("Real Estate Ads and Requests")

    # Section for browsing ads
    st.header("Browse Ads")

    for ad in ads_data:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(ad["Image"], use_column_width=True)

        with col2:
            st.write("**Title:**", ad["Title"])
            st.write("**Description:**", ad["Description"])
            st.write("**Type:**", ad["Type"])
            st.write("**Price:**", ad["Price"])
            st.write("**Contact:**", ad["Contact"])
            st.write("---")

    # Section for posting new ads
    st.header("Post a New Ad")
    with st.expander("Click here to post a new ad (+)"):
        ad_title = st.text_input("Ad Title")
        ad_description = st.text_area("Ad Description")
        ad_type = st.selectbox("Ad Type", ["Sell", "Rent"])
        ad_price = st.number_input("Price")
        ad_image = st.file_uploader("Upload Ad Image", type=["jpg", "png"])
        ad_contact = st.text_input("Contact Information")
        submitted = st.button("Submit Ad")

        if submitted:
            ads_data.append({
                "Title": ad_title,
                "Description": ad_description,
                "Type": ad_type,
                "Price": ad_price,
                "Image": ad_image,
                "Contact": ad_contact
            })
            st.success("Ad submitted successfully!")

    # Section for making requests
    st.header("Make a Request")
    with st.expander("Click here to make a request (+)"):
        selected_ad = st.selectbox("Select Ad", [ad["Title"] for ad in ads_data])
        requester_name = st.text_input("Your Name")
        requester_contact = st.text_input("Your Contact Information")
        submit_request = st.button("Submit Request")

        if submit_request:
            selected_ad_info = next(ad for ad in ads_data if ad["Title"] == selected_ad)
            requests_data.append({
                "Ad Title": selected_ad,
                "Requester Name": requester_name,
                "Requester Contact": requester_contact,
                "Advertiser Contact": selected_ad_info["Contact"]
            })
            st.success("Request submitted successfully!")

    # Section for displaying requests
    st.header("Requests")
    for request in requests_data:
        st.write("**Ad Title:**", request["Ad Title"])
        st.write("**Requester Name:**", request["Requester Name"])
        st.write("**Requester Contact:**", request["Requester Contact"])
        st.write("**Advertiser Contact:**", request["Advertiser Contact"])
        st.write("---")

elif menu_selection == "Other Services":
    st.title("Other Services")
    st.write("This is where you can explore other services.")

# Add more options to the menu as needed
