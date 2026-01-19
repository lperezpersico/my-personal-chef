import streamlit as st
from chef_agent import get_chef_agent
from utils import process_image_to_base64
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

# Page Configuration
st.set_page_config(page_title="My Personal Chef", page_icon=":woman_cook:")
st.title(":woman_cook: My Personal Chef")

# Initialize Agent and Vision Model
if "agent_executor" not in st.session_state:
    with st.spinner("Starting the Chef Agent..."):
        try:
            st.session_state.agent_executor = get_chef_agent()
        except Exception as e:
            st.error(f"Error starting the agent: {e}")
            st.stop()

model_vision = init_chat_model("llava:latest", model_provider="ollama")

# UI Layout
with st.container(border=True):
    col1, col2 = st.columns([1, 2])
    with col1:
        img_file = st.file_uploader("Upload ingredients image", type=["jpg", "png"], label_visibility="collapsed")
    with col2:
        user_msg = st.text_input("What are we cooking today?", placeholder="e.g., I want something healthy and fast")
    
    if st.button("Let's cook!", use_container_width=True):
        if "agent_executor" in st.session_state:
            detected_ingredients = ""
            
            # Step 1: Image Analysis (Vision Model)
            if img_file:
                with st.spinner("Analyzing the ingredients in the image..."):
                    try:
                        b64_img = process_image_to_base64(img_file)
                        
                        vision_message = HumanMessage(
                            content=[
                                {"type": "text", "text": "Identify all food ingredients in this image. List them clearly and concisely."},
                                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64_img}"}}
                            ]
                        )

                        vision_res = model_vision.invoke([vision_message])
                        detected_ingredients = vision_res.content
                        st.info(f"**Detected:** {detected_ingredients}")
                    except Exception as vision_err:
                        st.error(f"Vision Analysis Error: {vision_err}")

            # Step 2: Recipe Generation (Agentic Reasoning)
            with st.status("Chef is thinking...", expanded=True) as status:
                context_message = st.empty()
                context_message.write("Preparing cooking context...")
                
                final_prompt = (
                    f"Ingredients detected from image: {detected_ingredients}. "
                    f"User specific request: {user_msg}. "
                    f"Please suggest a professional recipe."
                )
                
                try:
                    response_container = st.empty()
                    full_response = ""

                    for chunk in st.session_state.agent_executor.stream(
                        {"messages": [HumanMessage(content=final_prompt)]},
                        config={"recursion_limit": 10},
                        stream_mode="values" 
                    ):
                        if "messages" in chunk:
                            context_message.empty()
                            last_message = chunk["messages"][-1]
                            
                            if last_message.type == "ai":
                                full_response = last_message.content
                                response_container.markdown(full_response)
                    
                    status.update(label="Chef has finished!", state="complete", expanded=True)
                    
                except Exception as e:
                    status.update(label="Thinking process failed", state="error", expanded=True)
                    st.error(f"Something went wrong: {e}")

        else:
            st.error("The agent is not ready. Please reload the page.")