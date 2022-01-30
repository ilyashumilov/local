const searchInput = document.getElementById('search1');
const panel = document.getElementById('variants_box1');


searchInput.addEventListener('keyup', function() {
    const name = searchInput.value;
    
    if (name != ''){
        var input = name[0].toUpperCase() + name.slice(1);
    }

    panel.innerHTML = '';
    const output = values1.filter(function(value1){
        return value1.startsWith(input);     
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

const searchInput1 = document.getElementById('search2');
const panel1 = document.getElementById('variants_box2');


searchInput1.addEventListener('keyup', function() {
    const name1 = searchInput1.value;
    
    if (name1 != ''){
       var input1 = name1[0].toUpperCase() + name1.slice(1);
    }

    panel1.innerHTML = '';
    const output1 = values2.filter(function(value2){
        return value2.startsWith(input1);     
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


const searchInput2 = document.getElementById('search3');
const panel2 = document.getElementById('variants_box3');


searchInput2.addEventListener('keyup', function() {
    const name2 = searchInput2.value;

    if (name2 != ''){
       var input2 = name2[0].toUpperCase() + name2.slice(1);
    }
    panel2.innerHTML = '';
    const output2 = values3.filter(function(value3){
        return value3.startsWith(input2);     
    });
    currentFocus = -1;
    output2.forEach(function(suggest2){
        const div2 = document.createElement('li');
        div2.innerHTML = suggest2;
        panel2.appendChild(div2);       
        
        div2.addEventListener('click', function(){
            searchInput2.value = suggest2;
            panel2.innerHTML = '';
        });

    });

    if (input2 == ''){
    panel2.innerHTML = '';
    }
})