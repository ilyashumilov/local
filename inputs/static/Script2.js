const searchInput = document.getElementById('search');
const panel = document.getElementById('variants');


searchInput.addEventListener('keyup', function() {
    const input = searchInput.value;

    
    panel.innerHTML = '';
    const output = countries.filter(function(country){
        return country.startsWith(input);     
    });
    currentFocus = -1;
    output.forEach(function(suggest){
        const div = document.createElement('div');
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

const searchInput1 = document.getElementById('search1');
const panel1 = document.getElementById('variants');
