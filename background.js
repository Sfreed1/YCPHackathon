// background.js
chrome.runtime.onInstalled.addListener(function() {
  });
  
  // Listen for a message from the popup
  chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
    if (message.action === "saveText") {
      // Execute script in the current tab to get the text of the webpage
      chrome.tabs.executeScript({
        code: 'document.body.innerText;'
      }, function(result) {
        // Error checking
        if (chrome.runtime.lastError || !result || !result.length) {
          sendResponse({error: 'Error fetching text from the page'});
          return;
        }
        
        // Send the text of the webpage to the server
        const textContent = result[0];
        fetch('http://localhost:3000/api/save-text', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ text: textContent })
        })
        .then(response => response.json())
        .then(data => {
          // Handle the response from your server
          console.log('Success:', data);
          sendResponse({data: 'Text saved successfully'});
        })
        .catch((error) => {
          console.error('Error:', error);
          sendResponse({error: 'Error occurred while saving text'});
        });
      });
    }
    // This return statement is necessary to use sendResponse asynchronously
    return true;
  });
  