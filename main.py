from llm_utils import extract_data, evaluate_data
from scratch import pdf_to_text

pdf = r'Blood report.pdf'

extracted_text = pdf_to_text(pdf)
extracted_data = extract_data(extracted_text)
print(extracted_data)
evaluation = evaluate_data(extracted_data)
print(evaluation)