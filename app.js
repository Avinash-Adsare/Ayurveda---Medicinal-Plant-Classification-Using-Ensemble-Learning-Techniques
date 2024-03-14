console.log('yes')
document.getElementById('uploadDiv').addEventListener('click', function() {
    let input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
  
    input.onchange = function(e) {
      let file = e.target.files[0];
      let formData = new FormData();
      formData.append('file', file);
  
      fetch('/upload', {
        method: 'POST',
        body: formData
      })
      .then(response => response.text())
      .then(result => {
        console.log(result);
      })
      .catch(error => {
        console.error('Error:', error);
      });
    };
  
    input.click();
  });