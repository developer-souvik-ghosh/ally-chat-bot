function generateChatHtml(chatObj){
    if(chatObj.destination == "yt"){
        var html = `<a href="`+ chatObj.data +`" target="_blank">`+ chatObj.data +`</a>`;
        showReceivedMessage(html)
        textToVoice("Your youtube video is opening")
        setTimeout(function () {
            window.open(chatObj.data, 'name');
        }, 500);
    }else if(chatObj.destination == "wiki"){
        if(chatObj.is_correct){
            showReceivedMessage(chatObj.data)
            textToVoice(chatObj.data)
            return chatObj.data;
        }else{
            showReceivedMultipleButton(chatObj.data)
            textToVoice("Please choose your options")
            return "Please choose your options";
        }
    }else if(chatObj.destination == "google"){
        showReceivedGSearch(chatObj.data)
        textToVoice("We found this results")
        return chatObj.data;
    }else{
        showReceivedMessage(chatObj.data)
        textToVoice(chatObj.data)
        return chatObj.data;
    }
}

function textToVoice(text){
    responsiveVoice.speak(text)
}

function showSendMessage(message){
    var currentTime = getCurrentTime()
    var html = `<div class="row message-body">
                <div class="col-sm-12 message-main-sender">
                    <div class="sender">
                        <div class="message-text">
                            `+ message +`
                        </div>
                        <span class="message-time pull-right">`+ currentTime +`</span>
                    </div>
                </div>
            </div>`;
    $('#mainChatConversation').append(html);
    $('#inputMessage').val("");
    moveToBottom()
}

function showReceivedMessage(message){
    var currentTime = getCurrentTime()
    var html = `<div class="row message-body">
                        <div class="col-sm-12 message-main-receiver">
                            <div class="receiver">
                                <div class="message-text">
                                    `+ message +`
                                </div>
                                <span class="message-time pull-right">`+ currentTime +`</span>
                            </div>
                        </div>
                    </div>`;
    $('#mainChatConversation').append(html)
    moveToBottom()
}

function showReceivedMultipleButton(buttonList){
    var html = "";
    for(var i=0; i<buttonList.length; i++){
        html = html + `<button type="button" class="btn btn-outline btnChooseOption">`+ buttonList[i] +`</button>`
    }

    var html = `<div class="row message-body">
                    <div class="col-sm-12 message-main-receiver">
                        `+ html +`
                    </div>
                </div>`;
    $('#mainChatConversation').append(html)
    moveToBottom()
}

function showReceivedGSearch(resultArray){
    var html = "";
    for(var i=0; i<resultArray.length; i++){
        if(i%2!=0){
            html = html + `<a href="`+ resultArray[i] +`" target="_blank" class="list-group-item list-group-item-action">`+ resultArray[i] +`</a>`
        }else{
            html = html + `<a href="`+ resultArray[i] +`" target="_blank" class="list-group-item list-group-item-action background-color-1">`+ resultArray[i] +`</a>`
        }
    }

    var html = `<div class="row message-body">
                    <div class="col-sm-12 message-main-receiver">
                        <div class="list-group">
                            `+ html +`
                        </div>
                    </div>
                </div>`;
    $('#mainChatConversation').append(html)
    moveToBottom()
}

function moveToBottom(){
    const element = document.getElementById("mainChatConversation");
    element.scrollTop = element.scrollHeight;
}