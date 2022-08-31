$(document).ready(function(){
    const button = document.getElementById('btnRecordMessage');
    button.addEventListener('click', () => {
      if (button.style['animation-name'] === 'flash') {
        recognition.stop();
        button.style['animation-name'] = 'none';
        // Start Animation
        $("#recordMic").removeClass("activate")
        content.innerText = '';
      } else {
        button.style['animation-name'] = 'flash';
        // Stop Animation
        recognition.start();
        $("#recordMic").addClass("activate")
      }
    });

    const content = document.getElementById('inputMessage');
    const recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.onresult = function (event) {
      let result = '';
      console.log(event.results.length)
      for (let i = event.resultIndex; i < event.results.length; i++) {
        result += event.results[i][0].transcript;
      }
      content.value = result;
      console.log(result)
    };
});

