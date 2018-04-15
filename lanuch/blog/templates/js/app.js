function sendData(){
  var xhttp = new XMLHttpRequest;
  xhttp.onreadystatechange = function() {
    if(this.readyStatus == 4 && this.status == 200){
    document.getElementById('demo').innerHTML = this.responseText;
  }
};
  xhttp.open("GET", "http://127.0.0.1:8000/home/", true)
  xhttp.send
}
