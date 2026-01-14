
import json
import sys

# Force utf-8 for stdout
sys.stdout.reconfigure(encoding='utf-8')

try:
    with open('Accident_Detection_NoteBook.ipynb', 'r', encoding='utf-8') as f:
        nb = json.load(f)

    print("Searching notebook for results...")

    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            # Check outputs
            if 'outputs' in cell:
                for output in cell['outputs']:
                    found = False
                    text_content = ""
                    if 'text' in output:
                        text_content = ''.join(output['text'])
                    elif 'data' in output and 'text/plain' in output['data']:
                        text_content = ''.join(output['data']['text/plain'])
                    
                    if text_content:
                        lower_text = text_content.lower()
                        if 'accuracy' in lower_text or 'precision' in lower_text or 'confusion' in lower_text or 'val_' in lower_text:
                            print("--- Cell Output ---")
                            print(text_content)
                            print("-------------------")
                            found = True

except Exception as e:
    print(f"Error: {e}")
