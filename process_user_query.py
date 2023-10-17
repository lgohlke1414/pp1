import openai
import PyPDF2
from decouple import config

# Set up your OpenAI API key
API_KEY = config('API_KEY')
print(API_KEY)
openai.api_key = API_KEY
pdf_file_path = r'C:\Users\lakeg\Desktop\TRU'
# Function to extract text from a PDF
def extract_text_from_pdf(pdf_file_path):
    text = ''
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    print(text)
    return text

# Function to generate a search query using GPT-3
def generate_search_query(user_input):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Generate a search query for materials based on user input: '{user_input}'",
        max_tokens=50,  # Adjust max_tokens as needed
        n = 1  # Number of completions to generate
    )
    return response.choices[0].text

# Example usage
if __name__ == '__main__':
    pdf_file_path = r'C:\Users\lakeg\Desktop\TRU\Danielle Simpkins.pdf'  # Replace with your PDF file
    user_input = input("Enter user query: ")

    # Extract text from the PDFho
    pdf_text = extract_text_from_pdf(pdf_file_path)

    # Generate a search query using GPT-3 based on user input
    search_query = generate_search_query(user_input)

    # Perform a search in your database using the generated search_query
    # Replace this with your actual database search logic

    # Display search results
    print("Search Results:")
    print("Search Query:", search_query)
    # Display search results based on your database search