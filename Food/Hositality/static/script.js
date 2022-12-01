
function myFunction() {
  var x = document.getElementById("password");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
function validateUserName(){
  var name = document.forms['registrationform']['username'].value;

  if(name=='' ||  name.length<5  || name.length>20){
    document.getElementById("username").style.border = "2px solid red";
    document.getElementById("errorname").style.color = "red";
    document.getElementById("errorname").innerHTML="UserName must contain 5 to 20 characters";
    return false;
  }
  else{
  document.getElementById("username").style.border = "2px solid green";
  document.getElementById("errorname").style.color = "green";
  document.getElementById("errorname").innerHTML="UserName Satisfied";
    return true;
  }
}

function validatePassword(){
    var password1 = document.forms['registrationform']['password'].value;
    var patt = new RegExp("[0-9]");
    var result = patt.test(password1);

    if(result==false || password1.length<5 || password1.length>20){
        document.getElementById("password").style.border = "2px solid red";
         document.getElementById("errorpassword").style.color = "red";
        var errorpassword1= "Password Must Contain 1 digit and should of length 5 to 20 ";
        document.getElementById("password").value="";
        document.getElementById("errorpassword").innerHTML=errorpassword1;
        return false;
    }
    else{
        document.getElementById("password").style.border = "2px solid green";
         document.getElementById("errorpassword").style.color = "green";
         var errorpassword2= "Constraints satisfied";

        document.getElementById("errorpassword").innerHTML=errorpassword2;
        return true;
    }
}
function validateEmail(){
     var email = document.forms['registrationform']['email'].value;

  if(email.includes('@gmail.com')){
  document.getElementById("email").style.border = "2px solid green";
  document.getElementById("erroremail").style.color = "green";
  document.getElementById("erroremail").innerHTML="Email is of required format";
    return true;
  }
  else{
  document.getElementById("email").style.border = "2px solid red";
    document.getElementById("erroremail").style.color = "red";
     document.getElementById("email").value="";
    document.getElementById("erroremail").innerHTML="The email should be of the form example@gmail.com";
    return false;
  }
}
function validateall(){
    if(validateUserName()  & validateEmail() & validatephone() & validatePassword()){
        return true;
    }else{
        return false;
    }
}