function SubmitFunction() {

    // Extract the question from input field
    let question = document.querySelector(".user-input-text").value
    console.log("Question: " + question)
    data = {"question":question}

    let answer = ''
    // Get answer from algorithm
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            answer = this.responseText

            // Generate new HTML consisting of question and answer
            let element = document.querySelector(".center-chat")
            element.innerHTML +=   `
                                    <div class="answer-container">
                                        <div class="answer">
                                            
                                            <div class="message-ans">
                                                <div class="bot-name">User</div>
                                                <div class="message-text">${question}</div>
                                            </div> 
                                            <div class="logo">Logo</div>
                                        </div>
                                    </div>
                                    <div class="question-container">
                                        <div class="question">
                                            <div class="logo">Logo</div>
                                            <div class="message">
                                                <div class="bot-name">GPT</div>
                                                <div class="message-text">${answer}</div>
                                            </div> 
                                        </div>
                                    </div>`
        }
        else{
            console.log(this.status)
        }
    }

    xhttp.open("POST", "http://127.0.0.1:8000/getAnswer/", true)
    xhttp.setRequestHeader('Content-type', 'application/json; charset=UTF-8');
    xhttp.send(data)

}