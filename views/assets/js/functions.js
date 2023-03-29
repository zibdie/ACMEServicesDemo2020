function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
 }

function MessageBoxDismissSend(statusID, messageID, boxDivID, messageShow)
{
    document.getElementById(statusID).setAttribute("style", "text-align: center; justify-content: center;");
    document.getElementById(statusID).setAttribute("src", "/assets/img/home_feed/loading.gif");
    document.getElementById(messageID).textContent = "Please Wait..."
    document.getElementById(messageID).setAttribute("style", "text-align: center; font-weight: bold");
    setTimeout(() => {
    document.getElementById(statusID).setAttribute("src", "/assets/img/home_feed/checkmark.png");
    document.getElementById(messageID).textContent = messageShow
    document.getElementById(messageID).setAttribute("style", "text-align: center; color: #00ff80; font-weight: bold;");
    }, 1000)

    setTimeout(() => { 
        $(boxDivID).modal('hide');
        document.getElementById(statusID).setAttribute("src", "data:image/gif;base64,R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="); 
        document.getElementById(messageID).textContent = " ";
        document.getElementById('exampleFormControlTextarea1').value = " "
    }, 3000)

}