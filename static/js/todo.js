function seterror(id , error){
    element = document.getElementsById(id);
    element.getElementsByClassName("formerror")[0].innerHTML = error;

}


function checkValidation(){
    var returnval = true;
    var name = document.forms['myForm']['ename'].value;
    if(name.length<5){
        seterror("name" , "length of name is too short")
        returnval = false;

    } 
    var email = document.forms['myForm']['eemail'].value;
    if(email.length > 15) {
        seterror("name" , "plz check email")
        returnval = false;

    }

    var email = document.forms['myForm']['mobile'].value;
    if(email.length != 10) {
        seterror("name" , "plz mobile number should be 10 digit")
        returnval = false;

    }


    return returnval
}