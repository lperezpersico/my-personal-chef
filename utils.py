from PIL import Image
import io
import base64

def process_image_to_base64(uploaded_file):
    """
    Processes an uploaded image file for AI model consumption.

    This function performs the following steps:
    1. Opens the image using PIL.
    2. Converts images with transparency (RGBA/P) to RGB to ensure JPEG compatibility.
    3. Resizes the image to a maximum of 250x250 pixels to optimize memory usage and processing speed.
    4. Encodes the processed image into a Base64 string.

    Args:
        uploaded_file (streamlit.runtime.uploaded_file_manager.UploadedFile): 
            The image file uploaded through the Streamlit UI.

    Returns:
        str: A UTF-8 encoded Base64 string representing the processed JPEG image.
    """
    img = Image.open(uploaded_file)
    
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    
    img.thumbnail((250, 250))
    
    buffered = io.BytesIO()
    img.save(buffered, format="JPEG")
    
    return base64.b64encode(buffered.getvalue()).decode('utf-8')