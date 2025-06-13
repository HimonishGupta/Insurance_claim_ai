def clean_text(text):
    return text.strip().replace('\n', ' ')

def extract_digits(string):
    return ''.join(filter(str.isdigit, string))
