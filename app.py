# Import required libraries
import streamlit as st

# Main function to create the dashboard
def main():
    # Set the page title and description
    st.title("Your AI Care Dashboard")
    st.markdown("Welcome to the Your AI Care Dashboard. Here, you can add your website!")

    # Problem Statement
    st.header("Problem Statement")
    st.markdown(
        "The urgent need for efficient and accurate disease detection from chest X-rays, "
        "particularly in resource-constrained regions like Myanmar and the ASEAN region, "
        "motivated us to develop 'YAiC.'"
    )
    st.markdown(
        "Respiratory diseases, such as COVID-19, tuberculosis, pneumonia, and lung cancer, "
        "have a devastating impact on lives and healthcare systems, leading to a pressing need for "
        "early intervention and improved healthcare outcomes."
    )

    # Solution
    st.header("Our Solution")
    st.markdown(
        "'YAiC' leverages deep learning and artificial intelligence to revolutionize disease detection "
        "from chest X-rays. Our automated system accurately identifies respiratory diseases, enabling "
        "early intervention and timely treatment. By reducing dependence on scarce human resources, "
        "we optimize healthcare services and empower healthcare providers worldwide."
    )

    # Sidebar section for website details
    st.sidebar.subheader("Add Website")
    website_url = st.sidebar.text_input("Enter the website URL:")
    website_name = st.sidebar.text_input("Enter the website name:")
    website_description = st.sidebar.text_area("Enter a brief description of the website:")
    website_category = st.sidebar.selectbox("Select the website category:", ["Healthcare", "Education", "Social Impact", "Other"])

    if st.sidebar.button("Add"):
        # Process the website details (you can add your own logic here, like saving to a database)
        # For this example, we'll just display the added website details.
        display_added_website(website_name, website_url, website_description, website_category)

# Function to display the added website details
def display_added_website(name, url, description, category):
    # You can add your own logic here, like saving to a database.
    # For this example, we'll simply display the website details in the dashboard.
    st.success("Website Successfully Added!")
    st.subheader("Website Details")
    st.markdown(f"**Name:** {name}")
    st.markdown(f"**URL:** [{url}]({url})")
    st.markdown(f"**Description:** {description}")
    st.markdown(f"**Category:** {category}")

# Run the main function
if __name__ == "__main__":
    main()
