const usernameArea=document.querySelector('#usernameArea');
const usernameField=document.querySelector('#usernameField');
const usernameFeedBackArea = document.querySelector('.username-feedback')
const emailArea=document.querySelector('#emailArea');
const emailField=document.querySelector('#emailField');
const emailFeedBackArea = document.querySelector('.email-feedback')
const usernameChecking = document.querySelector('.username-checking')
const passwordField=document.querySelector('#passwordField');
const showPassword = document.querySelector('#showPassword')
const submitBtn = document.querySelector('.submit-btn');


showPassword.addEventListener('click', function(){
    hangleToggleInput(passwordField, showPassword)
});

function hangleToggleInput(field, button) {
    if (button.classList.contains('.show')){
        button.classList.remove('.show');
        field.setAttribute('type', 'password')
    } else {
        button.classList.add('.show');
        field.setAttribute('type', 'text')
    };
    
};

emailField.addEventListener('keyup', (e) => {
    const emailVal = e.target.value;

    emailArea.classList.remove('is-invalid');
    emailArea.classList.remove('is-valid');
    emailFeedBackArea.style.display = 'none';
    emailFeedBackArea.innerHTML=``

    if (emailVal.length > 0) {
        emailArea.classList.add('is-valid');
        fetch('/auth/validate-email', {
            body: JSON.stringify({ 'email' : emailVal }),
            method: "POST",
        })
            .then((res) => res.json())
            .then((data) => { 
                if(data.email_error){
                    submitBtn.disabled = true;
                    emailArea.classList.remove('is-valid');
                    emailArea.classList.add('is-invalid');
                    emailFeedBackArea.style.display = 'block';
                    emailFeedBackArea.innerHTML=`<p>${data.email_error }</p>`

                } else {
                    submitBtn.removeAttribute("disabled");
                }
            });
    }

})

usernameField.addEventListener('keyup', (e) => {
    const usernameVal = e.target.value;

    usernameArea.classList.remove('is-invalid');
    usernameArea.classList.remove('is-valid');
    usernameFeedBackArea.style.display = 'none';
    usernameFeedBackArea.innerHTML=``
    

    if (usernameVal.length > 0) {
        usernameChecking.style.display='block'
        usernameChecking.textContent=`Checking ${usernameVal}`

        usernameArea.classList.add('is-valid');
        fetch('/auth/validate-username', {
            body: JSON.stringify({ 'username' : usernameVal }),
            method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                usernameChecking.style.display='none'
                
                if(data.username_error){
                    submitBtn.disabled = true;
                    usernameArea.classList.remove('is-valid');
                    usernameArea.classList.add('is-invalid');
                    usernameFeedBackArea.style.display = 'block';
                    usernameFeedBackArea.innerHTML=`<p>${data.username_error }</p>`

                } else {
                    submitBtn.removeAttribute("disabled");
                }
            });
    }
});