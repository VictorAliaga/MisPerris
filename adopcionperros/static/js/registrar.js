
function validate() {
	console.log("validando")
	var txtName = document.getElementById("txtName")
	var nameValidator = document.getElementById("nameValidator")
	console.log(txtName.value.split(' ').length)
	if(txtName.value.split(' ').length < 2){
		nameValidator.innerHTML = "Este campo debiese tener dos palabras al menos"
	} else {
		nameValidator.innerHTML = ""
	}
}