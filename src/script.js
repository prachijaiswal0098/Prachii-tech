function predictNews(){

document.getElementById("loading").style.display="block";

setTimeout(function(){

document.getElementById("loading").style.display="none";

document.getElementById("result").innerHTML="Prediction: Fake News";

},2000);

}
