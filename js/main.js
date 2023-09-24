document.addEventListener("DOMContentLoaded", function () {
    var chatElement = document.querySelector(".card");
    var messageInput = document.getElementById("message");
    var sendButton = document.getElementById("send");
    var chatMessages = document.getElementById("chat-messages");
  
    // Variable para almacenar los mensajes
    var messages = [];
  
    // Función para mostrar los mensajes en el chat y hacer scroll hacia abajo
    function displayMessages() {
      chatMessages.innerHTML = "";
      messages.forEach(function (message) {
        var li = document.createElement("li");
        li.className = "collection-item";
        li.innerText = message;
        chatMessages.appendChild(li);
      });
  
      // Hacer scroll hacia abajo
      chatMessages.scrollTop = chatMessages.scrollHeight;
    }
  
    // Función para enviar un mensaje
    function sendMessage() {
      var messageText = messageInput.value;
      if (messageText.trim() !== "") {
        messages.push("You: " + messageText);
        messageInput.value = "";
        displayMessages();
      }
    }
  
    // Evento para enviar un mensaje cuando se presione Enter
    messageInput.addEventListener("keypress", function (event) {
      if (event.key === "Enter") {
        sendMessage();
      }
    });
  
    // Evento para enviar un mensaje cuando se haga clic en el botón "Consultar"
    sendButton.addEventListener("click", sendMessage);
  
    // Mostrar el chat
    function showChat() {
      chatElement.classList.remove("hidden-chat");
      displayMessages();
    }
  
    // Ocultar el chat
    function hideChat() {
      chatElement.classList.add("hidden-chat");
    }
  
    // Clic abrir/ocultar
    document.getElementById("toggle-chat").addEventListener("click", function () {
      if (chatElement.classList.contains("hidden-chat")) {
        showChat();
      } else {
        hideChat();
      }
    });
  });