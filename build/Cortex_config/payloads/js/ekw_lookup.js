

let firstInput, secondInput, thirdInput, submit;

function procedure(){
    buildSelectors();
    setValues("WR1K","00334607","5");
    navigate();
}
function buildSelectors(){
    firstInput = document.getElementById("kodWydzialuInput");
    secondInput = document.getElementById("numerKsiegiWieczystej");
    thirdInput = document.getElementById("cyfraKontrolna");
    submit = document.getElementById("wyszukaj");
}



function setValues(first, second,third){
    firstInput.setAttribute('value',  first);
    secondInput.value=  second;
    thirdInput.setAttribute('value',  third);
}

function navigate(){
    submit.click();
    setTimeout(new function (){
        procedure();
    },100000)
}

procedure();

