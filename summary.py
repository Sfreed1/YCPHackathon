
import openai
import os

# Load your OpenAI API key from an environment variable for better security
# openai.api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = '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'



# for the text file
def summarize_text_and_identify_hazards(file_path, summary_length=300):
    # Read the content of the text file
    with open(file_path, 'r') as file:
        text_content = file.read()

    # The prompt now requests a summary and identification of potential hazards
    prompt_message = (
        "Summarize the following text in around 200 words and provide potential hazards or security concerns in around 100 words. Give bullet points and headings for each topic."
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

    # Split the content into summary and hazards
    summary, _, hazards = summary_and_hazards.partition("Potential Hazards:")

    # Replace newline characters with HTML line breaks for proper formatting
    summary_html = summary.replace('\n', '<br>')
    hazards_html = hazards.replace('\n', '<br>')

    # Write the results to an HTML file with CSS for better formatting
    with open('summary_and_hazards.html', 'w') as html_file:
        html_file.write(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Summary and Potential Hazards</title>
<style>
  body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    line-height: 1.6;
    padding: 20px;
  }}
  .container {{
    max-width: 800px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }}
  .section {{
    margin-bottom: 20px;
  }}
  .section h2 {{
    background-color: #0056b3;
    color: white;
    padding: 10px;
    border-radius: 4px;
  }}
  p {{
    background-color: #e7f4ff;
    padding: 10px;
    border-left: 5px solid #0056b3;
  }}
  button {{
    background-color: #0056b3;
    color: white;
    border: none;
    padding: 10px 20px;
    margin: 5px;
    border-radius: 5px;
    cursor: pointer;
  }}
  button:hover {{
    opacity: 0.8;
  }}
</style>
</head>
<body>
  <div class="container">
    <h1>Terms and Conditions Analysis</h1>
    <div class="section">
      <h2>Summary</h2>
      <p>{summary_html}</p>
    </div>
    <div class="section">
      <h2>Potential Hazards</h2>
      <p>{hazards_html}</p>
    </div>
    <div class="button-container">
      <button onclick="speakText('en-US')">Listen in English</button>
      <button onclick="speakText('es-ES')">Escuchar en Español</button>
      <button onclick="stopText()">Stop Audio</button>
    </div>
  </div>
  <script>
    var synth = window.speechSynthesis;
    function speakText(language) {{
      if (synth.speaking) {{
          synth.cancel(); // Stop any currently speaking audio
      }}
      var summaryText = document.querySelector('.section:nth-child(2) p').textContent;
      var hazardsText = document.querySelector('.section:nth-child(3) p').textContent;
      var textToSpeak = summaryText + " " + hazardsText;
      var utterThis = new SpeechSynthesisUtterance(textToSpeak);
      utterThis.lang = language; // Set the language
      synth.speak(utterThis);
    }}

    function stopText() {{
      synth.cancel();
    }}
  </script>
</body>
</html>''')

    return 'summary_and_hazards.html'

file_path = 'ex.txt'
html_file = summarize_text_and_identify_hazards(file_path)
print(f"Results have been written to {html_file}")

