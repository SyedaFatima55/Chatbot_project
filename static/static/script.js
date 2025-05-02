function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    var chatBox = document.getElementById("chat-box");

    if (userInput.trim() === "") return;

    chatBox.innerHTML += "<div><b>You:</b> " + userInput + "</div>";


    fetch('/get?msg=' + userInput)
    .then(response => response.text())
    .then(function(botReply) {
        chatBox.innerHTML += "<div><b>Bot:</b> " + botReply + "</div>";
        chatBox.scrollTop = chatBox.scrollHeight;  
    });

    document.getElementById("user-input").value = "";  
}
