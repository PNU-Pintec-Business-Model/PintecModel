/*!
    * Start Bootstrap - SB Admin v7.0.5 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2022 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

var predictVal=1500;
var actualVal=1800;
var today;
var nextday;
var nextdayPred=2000;

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

function CalculateError() {

    var error = document.getElementById("errorval");

    if (predictVal>actualVal) {
        //blue
        error.innerHTML += " -";
        error.style.color = "blue";
    } else {
        //red
        error.innerHTML += " +";
        error.style.color = "red";
    }

    var errorVal=Math.abs(predictVal-actualVal);
    return error.innerHTML+errorVal;
}

function printDate() {

    const day = new Date();
    const year = day.getFullYear();
    const month = day.getMonth()+1;
    const date = day.getDate();
    const nextdate = day.getDate()+1;

    today = year +"."+ month +"."+ date;
    nextday = year +"."+ month +"."+ nextdate;

    return today;
}

printDate();

function printResult() {

    var str = nextday +"(내일) 새송이(특) 예측값은 <span style='color: red;'>" + nextdayPred + "</span>으로 \
                        어제보다 1000원 인상될 것으로 예측됩니다." ;

    return str;
}

document.getElementById("dates").innerHTML = today+"(오늘)";
document.getElementById("errorval").innerHTML += CalculateError();
document.getElementById("result").innerHTML = printResult();