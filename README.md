# YCPHackathon
Terms and Conditions Summarization Script
This script, titled "summary.py," is designed to summarize terms and conditions documents to help users better understand their content. It utilizes OpenAI's GPT-3.5 Turbo model to generate concise summaries and identify potential hazards or security concerns within the text. The summarized information is then formatted into an HTML document for easy reading.

Prerequisites
Before using this script, make sure you have the following prerequisites:

Python installed on your system.
An OpenAI API key stored in an environment variable named OPENAI_API_KEY.
Usage
Place your terms and conditions document in a text file. In this example, the file is named "ex.txt."

Customize the length of the summary by adjusting the summary_length parameter in the script.

Run the script by executing the following command in your terminal:

python summary.py

The script will send the document to the OpenAI API, generate a summary, and identify potential hazards.

The results will be saved in an HTML file named "summary_and_hazards.html."

Understanding the Output
The generated HTML file contains two sections:

Summary: This section provides a summarized version of the terms and conditions from the input document.

Potential Hazards: This section identifies potential hazards or security concerns found in the document.

Additional Features
The HTML file also includes the ability to listen to the summary and hazards in English or Spanish. You can click the provided buttons to hear the content read aloud.

Customization
Feel free to modify the script to suit your specific use case or further customize the HTML formatting.
