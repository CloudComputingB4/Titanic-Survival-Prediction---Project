
function displayTravel(){
    var elem_age = document.getElementsByName("Age")[0].value;
    var TravelAlone = document.getElementsByName("TravelAlone");
    displayNameTitle()
    if (parseInt(elem_age) < 16){
        document.getElementsByClassName('label_TravelAlone')[0].innerHTML = "";
        document.getElementsByName("TravelAlone")[0].style.display = "none";
        TravelAlone[1].checked = true
        displayRadioValue()

    }else{
        document.getElementsByClassName('label_TravelAlone')[0].innerHTML = "Yes";
        document.getElementsByName("TravelAlone")[0].style.display = "inline-block";

        var elem2 = document.getElementsByName("TravelNum")[0].value;
        if (elem2 == ""){
            TravelAlone[1].checked = false
            displayRadioValue()
        }
    }
}


function displayRadioValue() {
    var ele = document.getElementsByName('TravelAlone');
     
    if (ele[1].checked == true){
        document.getElementById("trav_pers").style.display = "block";
    }else{
        document.getElementById("trav_pers").style.display = "none";
        document.getElementsByName("TravelNum")[0].value = ""
    }
}

function displayNameTitle() {
    var elem_pclass = document.getElementsByName("Pclass");
    var elem_gender = document.getElementsByName("Sex");
    var elem_age = document.getElementsByName("Age")[0].value;

    if(elem_pclass[2].checked == true){
        document.getElementsByClassName('label_NameTitle')[3].innerHTML = "";
        document.getElementsByClassName('label_NameTitle')[4].innerHTML = "";
        document.getElementsByName("NameTitle")[3].style.display = "none";
        document.getElementsByName("NameTitle")[4].style.display = "none";

    }else if(elem_pclass[0].checked == true || elem_pclass[1].checked == true){
        document.getElementsByClassName('label_NameTitle')[3].innerHTML = "Master.";
        document.getElementsByClassName('label_NameTitle')[4].innerHTML = "Other Title";
        document.getElementsByName("NameTitle")[3].style.display = "inline-block";
        document.getElementsByName("NameTitle")[4].style.display = "inline-block";
    }

    if(elem_gender[0].checked == true && parseInt(elem_age) <= 21){
        document.getElementsByClassName('label_NameTitle')[0].innerHTML = "";
        document.getElementsByClassName('label_NameTitle')[1].innerHTML = "Miss.";
        document.getElementsByClassName('label_NameTitle')[2].innerHTML = "";
        document.getElementsByClassName('label_NameTitle')[3].innerHTML = "";

        document.getElementsByName("NameTitle")[0].style.display = "none";
        document.getElementsByName("NameTitle")[1].style.display = "inline-block";
        document.getElementsByName("NameTitle")[2].style.display = "none";
        document.getElementsByName("NameTitle")[3].style.display = "none";

    }else if(elem_gender[0].checked == true && parseInt(elem_age) > 21 || elem_gender[0].checked == true && elem_age == ""){
        document.getElementsByClassName('label_NameTitle')[0].innerHTML = "";
        document.getElementsByClassName('label_NameTitle')[1].innerHTML = "Miss.";
        document.getElementsByClassName('label_NameTitle')[2].innerHTML = "Mrs.";
        document.getElementsByClassName('label_NameTitle')[3].innerHTML = "";

        document.getElementsByName("NameTitle")[0].style.display = "none";
        document.getElementsByName("NameTitle")[1].style.display = "inline-block";
        document.getElementsByName("NameTitle")[2].style.display = "inline-block";
        document.getElementsByName("NameTitle")[3].style.display = "none";

    }else if(elem_gender[1].checked == true){
        document.getElementsByClassName('label_NameTitle')[0].innerHTML = "Mr.";
        document.getElementsByClassName('label_NameTitle')[1].innerHTML = "";
        document.getElementsByClassName('label_NameTitle')[2].innerHTML = "";
        document.getElementsByClassName('label_NameTitle')[3].innerHTML = "Master.";     
        
        document.getElementsByName("NameTitle")[0].style.display = "inline-block";
        document.getElementsByName("NameTitle")[1].style.display = "none";
        document.getElementsByName("NameTitle")[2].style.display = "none";
        document.getElementsByName("NameTitle")[3].style.display = "inline-block";
    }   
} 

function functionAlert(msg) {
    var confirmBox = $("#confirm");
    confirmBox.find(".message").text(msg);
    confirmBox.find(".yes").unbind().click(function() {
       confirmBox.hide();
    });
    confirmBox.show();
 }

function validate() {
    let empty_count = 0

    var Pclass = document.getElementsByName("Pclass");
    var Cabin = document.getElementsByName("Cabin");
    var Age = document.getElementsByName("Age")[0].value;
    var Sex = document.getElementsByName("Sex");
    var Embarkation = document.getElementsByName("Embarkation");
    var NTitle = document.getElementsByName("NameTitle");
    var TravelAlone = document.getElementsByName("TravelAlone");

    let Pclass_count = 0
    let Cabin_count = 0
    let Sex_count = 0
    let Embarkation_count = 0
    let NTitle_count = 0
    let TravelAlone_count = 0

    for(i = 0; i < Pclass.length; i++) {
        if(Pclass[i].checked == true)
            Pclass_count = Pclass_count + 1
    }

    for(i = 0; i < Cabin.length; i++) {
        if(Cabin[i].checked == true)
            Cabin_count = Cabin_count + 1
    }

    for(i = 0; i < Sex.length; i++) {
        if(Sex[i].checked == true)
            Sex_count = Sex_count + 1
    }

    for(i = 0; i < Embarkation.length; i++) {
        if(Embarkation[i].checked == true)
        Embarkation_count = Embarkation_count + 1
    }

    for(i = 0; i < NTitle.length; i++) {
        if(NTitle[i].checked == true)
            NTitle_count = NTitle_count + 1
    }

    for(i = 0; i < TravelAlone.length; i++) {
        if(TravelAlone[i].checked == true)
            TravelAlone_count = TravelAlone_count + 1
    }

    if (Pclass_count == 0){
        empty_count = empty_count + 1
        var message = "Please Provide a Ticket Class!"
    }

    if (Cabin_count == 0){
        empty_count = empty_count + 1
        var message = "Please Provide a Cabin answer!"
    }

    if (Age == ""){
        empty_count = empty_count + 1
        var message = "Please Provide an Age!"
    }

    if (Sex_count == 0){
        empty_count = empty_count + 1
        var message = "Please Provide a Gender!"
    }

    if (Embarkation_count == 0){
        empty_count = empty_count + 1
        var message = "Please Provide a Port of Embarkation!"
    }

    if (NTitle_count == 0){
        empty_count = empty_count + 1
        var message = "Please Provide a Name Title!"
    }

    if (TravelAlone_count == 0){
        empty_count = empty_count + 1
        var message = "Please Provide a Travel Answer!"
    }

    if (TravelAlone[1].checked == true){
        var elem2 = document.getElementsByName("TravelNum")[0].value;
        if (elem2 == ""){
            empty_count = empty_count + 1
            var message = "Please Provide a Travel Relative Number!"
        }
    }
    
    if (empty_count == 1){
        functionAlert(message)
        return false;
        
    }else if (empty_count > 1){
        var message = "You must fill all the fields!";
        functionAlert(message)

        return false;
    }else{
        return true;
    }
}


function randomFill() {
    var Pclass = document.getElementsByName("Pclass");
    var Cabin = document.getElementsByName("Cabin");
    var Gender = document.getElementsByName("Sex");
    var Embarkation = document.getElementsByName("Embarkation");
    var NTitle = document.getElementsByName("NameTitle");
    var TravelAlone = document.getElementsByName("TravelAlone");

    i_Pclass = Math.floor(Math.random() * Pclass.length);
    i_Cabin = Math.floor(Math.random() * Cabin.length);
    i_Gender = Math.floor(Math.random() * Gender.length);
    i_Embarkation = Math.floor(Math.random() * Embarkation.length);
    i_NTitle = Math.floor(Math.random() * NTitle.length);
    i_TravelAlone = Math.floor(Math.random() * TravelAlone.length);

    Pclass[i_Pclass].checked = true
    Cabin[i_Cabin].checked = true
    document.getElementsByName("Age")[0].value = Math.floor(Math.random() * 75);
    Gender[i_Gender].checked = true
    Embarkation[i_Embarkation].checked = true
    NTitle[i_NTitle].checked = true
    TravelAlone[i_TravelAlone].checked = true

    displayRadioValue()
    if (TravelAlone[1].checked == true){
        document.getElementsByName("TravelNum")[0].value = Math.floor(Math.random() * 6) + 1;
    }
}   

