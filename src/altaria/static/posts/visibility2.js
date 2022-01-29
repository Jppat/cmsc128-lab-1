const visibilityToggle1 = document.getElementById('toggle-icon1');
const visibilityToggle2 = document.getElementById('toggle-icon2');
const input1 = document.getElementById('user-password1');
const input2 = document.getElementById('user-password2');

var password1 = true;
var password2 = true;

visibilityToggle1.addEventListener('click', function(){
	if(password1){
		input1.setAttribute('type', 'text');
		visibilityToggle1.className = 'fas fa-eye-slash'
	} else {
		input1.setAttribute('type', 'password');
		visibilityToggle1.className = 'fas fa-eye'
	}
	password1 = !password1;

});

visibilityToggle2.addEventListener('click', function(){
	if(password2){
		input2.setAttribute('type', 'text');
		visibilityToggle2.className = 'fas fa-eye-slash'
	} else {
		input2.setAttribute('type', 'password');	
		visibilityToggle2.className = 'fas fa-eye'
	}
	password2 = !password2;

});