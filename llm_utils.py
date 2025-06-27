from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGroq(
    model = "llama3-70b-8192",
    temperature=0,
    api_key="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"
)
def extract_data(extracted_text):
    prompt_extract = ChatPromptTemplate.from_messages([
        ("system", """ I will give you unstructured text from a blood test report. Your job is to extract each test with the following details:
        - "Test Name"
        - "Value"
        - "Unit"
        - "Reference Range"

    For each test:
        - Carefully extract the value.
        - Cross-check whether the value falls within or near the reference range.
        - If the value appears *significantly outside* the reference range (e.g. 2x higher or lower), assume it may be a possible OCR error.
        - In such cases, include a key called "Suspected OCR Error" with value true.
        - Optionally suggest a corrected value as "Estimated Value" if it can be reasonably inferred.

    Make sure every item contains a valid "Value".

    Format your reply in valid JSON — a list of objects as described.
    Do not include any explanation, notes, or commentary outside of the JSON structure"""),
        ("human", "{extracted_text}")

    ])

    chain_extract = prompt_extract | llm
    result = chain_extract.invoke({"extracted_text": extracted_text})
    result = result.content
    return result

def evaluate_data(extracted_data):
    prompt_evaluate = ChatPromptTemplate.from_messages([
        ("system", """
                    You are a medical report analyzer you will help patients with their blood report
                    You will be the medical report in a JSON Format.. your job is to analyze that data 
                    and give them a professional evaluation"""),

        ("human", "{extracted_data}")
    ])

    chain_evaluate = prompt_evaluate | llm
    result = chain_evaluate.invoke({"extracted_data" : extracted_data})
    result = result.content
    return result