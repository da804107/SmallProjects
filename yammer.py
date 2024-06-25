import pandas as pd
import re

data = pd.read_csv(r"C:\Users\hernandezgonzalezd\PycharmProjects\yammerPractice\venv\2023 Yammer.csv")
#print(data.head())


def clean_body(text):
    if isinstance(text, str):
        # Remove HTTP tags and image URLs using regular expressions
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)  # Remove URLs starting with HTTP
        text = re.sub(r'[?^\x00-\x7F]+', '', text)  # Remove weird characters
        return text.strip()
    return text


# apply the function to the relevant column
data_cleaned = data['body'].apply(clean_body)


#print(data['body'].head())

# save the cleaned DataFrame back to a csv file
cleaned_file_path = r'C:\Users\hernandezgonzalezd\PycharmProjects\yammerPractice\venv\cleanedYammer.csv'
data.to_csv(cleaned_file_path, index=False)

print("Body cleaned and CSV file saved.")
