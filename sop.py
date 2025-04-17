import streamlit as st
from image_processor import ImageProcessor
from llm_client import LLMClient

def initialize_session_state():
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'current_image_content' not in st.session_state:
        st.session_state.current_image_content = None

def main():
    st.set_page_config(page_title="Image Analysis Chatbot", layout="wide")
    st.title("Image Analysis Chatbot")
    
    initialize_session_state()
    
    # Initialize components
    image_processor = ImageProcessor()
    llm_client = LLMClient()
    
    # Create two columns
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.header("Image Upload")
        uploaded_image = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])
        
        if uploaded_image:
            st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
            
            # Process the image
            with st.spinner("Processing image..."):
                try:
                    extracted_content = image_processor.extract_text_and_tables(uploaded_image)
                    st.session_state.current_image_content = image_processor.get_formatted_content()
                    
                    with st.expander("View Extracted Content"):
                        st.text(st.session_state.current_image_content)
                    
                    st.success("Image processed successfully!")
                except Exception as e:
                    st.error(f"Error processing image: {str(e)}")
    
    with col2:
        st.header("Chat Interface")
        
        # Chat Interface
        user_input = st.text_input("Ask a question about the image:")
        
        if st.button("Send") and user_input:
            if st.session_state.current_image_content:
                with st.spinner("Generating response..."):
                    try:
                        # Generate response using the LLM
                        response = llm_client.generate_response(
                            prompt=user_input,
                            context=st.session_state.current_image_content
                        )
                        
                        # Add to chat history
                        st.session_state.chat_history.append(("user", user_input))
                        st.session_state.chat_history.append(("bot", response))
                    except Exception as e:
                        st.error(f"Error generating response: {str(e)}")
            else:
                st.warning("Please upload an image first!")
        
        # Display chat history
        st.subheader("Chat History")
        for role, message in st.session_state.chat_history:
            if role == "user":
                st.write("🧑 You:", message)
            else:
                st.markdown("🤖 **Assistant:**")
                st.markdown(message)
                st.markdown("---")

if __name__ == "__main__":
    main()
