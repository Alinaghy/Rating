document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#comments').style.display = "none";
    document.addEventListener('click', event => {

        const element = event.target;
        if (element.className === 'watchlist'){
            const i = element.id;
            fetch(`/update/watchlist`, {
            method: 'POST',
            body: JSON.stringify({
                id : i
                
            })
            })
            if(element.innerText == "Remove from watchlist"){
                element.innerHTML = "Add to watchlist";
            }
            else{
                element.innerHTML = "Remove from watchlist";
            }


        }

        if (element.className === 'rating'){
            const i = element.id;
            var m = document.getElementsByClassName('rating').value;
            const r = parseInt(m);
            fetch('/rate', {
            method: 'POST',
            body: JSON.stringify({
                id : i,
                rate : r
                
            })
            })
            .then(response =>response.json())
            .then(result => {
                if (result.E){
                    document.querySelector('#error').innerHTML = `* ${result.E}`;
                }
            });
        }

        if (element.className === 'b-comment'){
            const i = element.id;
            var c = document.getElementById('comment').value;
            fetch('/comment', {
            method: 'POST',
            body: JSON.stringify({
                id : i,
                comment : c
                
            })
            })
            document.getElementById('comment').value = "";
            document.querySelector('#ex-com').innerHTML = `{{ user.username }} : ${c}`;
        }

        if (element.className === 'comment-b'){
            document.querySelector('#comments').style.display = "block";
        }

        if (element.id === 'b-search'){
            var x = document.getElementById('search').value()
            fetch(`/movie_page/${x}`, {
            method: 'GET',
            body: JSON.stringify({
            })
            })  
        }


    });

});