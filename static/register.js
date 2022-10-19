






function sendToDB(e,u, p){
    
  
  
  


  const request = new Request(method='POST')

  fetch('/backend/register/', {
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
    email: e, 
    username: u,
    password: p
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
      window.location.href = "http://127.0.0.1:8000/login/"
    }
    else{
      console.log("nao autenticado")
        

    }
  }).catch(function(error){console.warn('error ', error);
}
); 
}