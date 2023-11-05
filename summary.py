import openai
import os

# Load your OpenAI API key from an environment variable for better security

openai.api_key = os.getenv('OPENAI_API_KEY')



def summarize_text_and_identify_hazards(file_path, summary_length=270):
    # Read the content of the text file
    with open(file_path, 'r') as file:
        text_content = file.read()

    # The prompt now requests a summary and identification of potential hazards
    prompt_message = (
        "Summarize the following text and provide potential hazards or security concerns."
    )

    # Send the text to the OpenAI API and request the desired information
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt_message},
            {"role": "user", "content": text_content}
        ],
        max_tokens=summary_length
    )

    # Extract the requested information from the response
    summary_and_hazards = response['choices'][0]['message']['content']

    # Write the results to an HTML file
    with open('summary_and_hazards.html', 'w') as html_file:
        html_file.write('<html><head><title>Summary and Potential Hazards</title></head>\n')
        html_file.write('<body>\n')
        html_file.write('<h1>Summary and Potential Hazards</h1>\n')
        html_file.write('<ul>\n')
        for line in summary_and_hazards.split('\n'):
            html_file.write(f'<li>{line}</li>\n')
        html_file.write('</ul>\n')
        html_file.write('</body></html>')

    return 'summary_and_hazards.html'

# Usage
file_path = 'ex.txt'
html_file = summarize_text_and_identify_hazards(file_path)
print(f"Results have been written to {html_file}")

