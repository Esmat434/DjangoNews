function submit_google(){
    document.getElementById("google_form").submit()
}

function submit_facebook(){
    document.getElementById("facebook_form").submit()
}

document.getElementById('closeErrorCard').addEventListener('click', function() {
    document.getElementById('errorCard').style.display = 'none';
});