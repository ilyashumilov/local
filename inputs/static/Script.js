const searchInput = document.getElementById('POL');
const panel = document.getElementById('variants');


searchInput.addEventListener('keyup', function() {
    const name = searchInput.value;
    
    if (name != ''){
        var input = name[0].toUpperCase() + name.slice(1);
    }
    
    panel.innerHTML = '';
    const output = countries.filter(function(country){
        return country.startsWith(input);     
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

const searchInput1 = document.getElementById('POD');
const panel1 = document.getElementById('variants1');


searchInput1.addEventListener('keyup', function() {
    const name1 = searchInput1.value;
    
    if (name1 != ''){
        var input1 = name1[0].toUpperCase() + name1.slice(1);
    }
    
    panel1.innerHTML = '';
    const output1 = countries1.filter(function(country1){
        return country1.startsWith(input1);     
    });
    currentFocus = -1;
    output1.forEach(function(suggest1){
        const div1 = document.createElement('li');
        div1.innerHTML = suggest1;
        panel1.appendChild(div1);       
        
        div1.addEventListener('click', function(){
            searchInput1.value = suggest1;
            panel1.innerHTML = '';
        });

    });

    if (input1 == ''){
    panel1.innerHTML = '';
    }
})
