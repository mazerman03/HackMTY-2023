from js import document


def translate_english(event):
    input_text = document.querySelector("#message")
    answer = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = "Hola, esta es tu respuesta"