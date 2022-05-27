const productBox = document.querySelectorAll('.price');
productBox.forEach((list,index) =>{
    const discountPrice = list.querySelector('.descount');
    const realPrice = list.querySelector('.real');
    let percent = list.querySelector('.percent');
    if (discountPrice.innerText.length>1) {
        realPrice.setAttribute('style','text-decoration: line-through;');
        let amount1 = realPrice.innerHTML;
        let amount2 = discountPrice.innerHTML;
        amount1= amount1.substring(1);
        amount2= amount2.substring(1);
        let how = 100-((amount2 * 100)/amount1);
        percent.innerHTML = " (-"+how.toFixed(1)+"%)"
    }
    else{
        discountPrice.setAttribute('style','display: none;')
    }
});

