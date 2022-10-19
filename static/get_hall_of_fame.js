/*
    Script que faz um request à API REST, obtém os dados do top10 leaderboard e expõe no HTML
*/

fetch("http://127.0.0.1:8000/backend/halloffame/").then((data)=>{
    //console.log(data);
    return data.json();
}).then((top_users_array)=>{
    // console.log(top_users_array)
    // console.log(Object.keys(top_users_array))

    let data = "";
    let user_data = "";
    Object.keys(top_users_array).map((place)=>{

        if(place != 'user_place'){
            data += `<li>
            <h2>${top_users_array[place].nome} ${top_users_array[place].nr_respostas_corretas}</h2>
            </li>`
        }  
        else{
            user_data += `<span>
            <h2>${top_users_array[place].place}. ${top_users_array[place].nome} ${top_users_array[place].nr_respostas_corretas}</h2>
            </span>`
        }

    })

    document.getElementById("leaderboard").innerHTML = data;
    document.getElementById("user_place").innerHTML = user_data;

}).catch((err)=>{
    console.log(err);
})