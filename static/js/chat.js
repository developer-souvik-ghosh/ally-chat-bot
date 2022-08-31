$(document).ready(function(){
    $(document).on('keyup', "#inputMessage", function(e){
        if (e.key === 'Enter' || e.keyCode === 13) {
            var inputMessage = $.trim($('#inputMessage').val());
            if(inputMessage != ""){
                callSendMessageAPI(inputMessage)
            }
        }
    });

    $(document).on('click', ".btnChooseOption", function(event){
        var selectOption = $(this).text()
        callSendMessageAPI("wiki " + selectOption)
    });

    $(document).on('click', "#btnSendMessage", function(event){
        var inputMessage = $.trim($('#inputMessage').val());
        if(inputMessage != ""){
            callSendMessageAPI(inputMessage)
        }
    });
});

function callSendMessageAPI(message){
    var buttonID = "#btnSendMessage";
    var formData = new FormData();
    formData.append('command', message);

    $.ajax({
        async: true,
        type: "POST",
        url: "/api/v1/voice/query",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        beforeSend: function() {
            $(buttonID).prop('disabled', true);
            showSendMessage(message)
        },
        success: function (data) {
            console.log(data)
            $(buttonID).prop('disabled', false);
            if(data.status){
                generateChatHtml(data)
            }else{
                textToVoice(data.message)
                showReceivedMessage(data.message)
            }
        },
        error: function(request, status, error) {
            $(buttonID).prop('disabled', false);
        }
  });
}

function getCurrentTime(){
    var currentdate = new Date();
    var datetime = currentdate.getDate() + "-" + (currentdate.getMonth()+1)  + "-" + currentdate.getFullYear() + " "
                    + currentdate.getHours() + ":" + currentdate.getMinutes() + ":" + currentdate.getSeconds();
    return datetime;
}