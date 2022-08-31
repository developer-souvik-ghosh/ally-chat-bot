$(document).ready(function(){
    $(document).on("click", "#btnInputBox", function(e){
         textToVoice($('#textInputBox').val())
    });
});

function textToVoice(text){
    responsiveVoice.speak(text)
}