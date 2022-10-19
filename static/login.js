


function escreve(a, b) {
    
    console.log(a);
    console.log(b);
  }



function sendToDB(e, p){
  
  
  
  const loginErrorMsg = document.getElementById("login-error-msg");

  const request = new Request(method='POST')

  fetch('/backend/login/', {
  method: 'POST',  
  headers: 
  {
   'Content-Type': 'application/json',
    'Host': 'localhost:8000',
    
    'Connection': 'keep-alive',
   
    'Accept': 'application/json, */*;q=0.5'
  },
  body:  JSON.stringify(
    {
    username: e,
    password: p,
}
  )}).then(function(response){
    if(response.ok){
      return response.json();
    }else{
      
      return Promise.reject(response);
    }
    
  }).then(function (data){
    if(data['autenticado'] == 'true'){
      console.log("autenticado")
      window.location.href = "http://127.0.0.1:8000/halloffame/"
    }
    else{
      console.log("nao autenticado")
      loginErrorMsg.style.opacity = 1;

    }
  }).catch(function(error){console.warn('error ', error);
}
); 
}