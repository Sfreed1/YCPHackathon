document.getElementById('saveText').addEventListener('click', () => {
  chrome.tabs.executeScript({
    code: 'document.body.innerText;'
  }, (result) => {
    if (chrome.runtime.lastError || !result || result.length === 0) {
      console.error('Error fetching text from the page:', chrome.runtime.lastError);
      return;
    }

    fetch('http://localhost:3000/api/save-text', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text: result[0] })
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  });
});
