const searchInput = document.getElementById('search');
const panel = document.getElementById('variants');
searchInput.value = current;

searchInput.addEventListener('keyup', function() {
    const name = searchInput.value
    
    if (name != ''){
        var input = name[0].toUpperCase() + name.slice(1);
    };
    
    panel.innerHTML = '';
    const output = values.filter(function(value){
        return value.startsWith(input);     
    });
    currentFocus = -1;
    output.forEach(function(suggest){
        const div = document.createElement('li');
        div.innerHTML = suggest;
        panel.appendChild(div);       
        
        div.addEventListener('click', function(){
            searchInput.value = suggest;
            panel.innerHTML = '';
        });

    });

    if (input == ''){
    panel.innerHTML = '';
    }
})

