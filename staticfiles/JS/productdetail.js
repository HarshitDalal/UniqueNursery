const minus = document.getElementById('minus');
const plus = document.getElementById('plus');

plus.addEventListener('click',()=>{
    let valu = document.getElementById('quantity').value;
    if (valu == 100) {
        document.getElementById('quantity').value = 100;
        alert("Max Quantity Added.")
    } else {
        document.getElementById('quantity').value = Number(valu)+1;
        document.getElementById('$id_quantity').value = Number(valu)+1;
    }
})
minus.addEventListener('click',()=>{
    let valu = document.getElementById('quantity').value;
    if (valu == 1) {
        alert("At Least 1 Quantity Requried.")
        document.getElementById('quantity').value = 1;    
    } else {
        document.getElementById('quantity').value = Number(valu)-1;
        document.getElementById('$id_quantity').value = Number(valu)-1;
    }
})

