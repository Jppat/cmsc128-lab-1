const visibilityToggle = document.getElementById('toggle-icon');
const input = document.getElementById('user-password');


var password = true;
visibilityToggle.addEventListener('click', function(){
	if(password){
		input.setAttribute('type', 'text');
		visibilityToggle.className = 'fas fa-eye-slash'
	} else {
		input.setAttribute('type', 'password');
		visibilityToggle.className = 'fas fa-eye'
	}
	password = !password;

});