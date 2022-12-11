let file;
const inputfile = document.getElementById('prodimg');
const secondimg = document.getElementById('secondimg');
let yes = true;

inputfile.addEventListener('change',()=>{
    file = inputfile.files[0];
    let fileType = file.type;
    let url = URL.createObjectURL(file);
    let validExtensions = ["image/png"];
    if(validExtensions.includes(fileType)){
        document.getElementById('productimg').innerHTML =  `<img src="${url}" alt="">`;
    }
    else{
        alert('Only PNG File Allow . After Click Ok Select New File.');
        window.location.reload()
    }
});



secondimg.addEventListener('change',()=>{
    file = secondimg.files[0];
    let fileType = file.type;
    let url = URL.createObjectURL(file);
    let validExtensions = ["image/jpeg","image/jfif","image/jpg"];
    if(validExtensions.includes(fileType)){
        document.getElementById('secondimage').src = url;
    }
    else{
        alert('Only JPEG, JFIF, JPG File Allow .After Click Ok Select New File.');
        window.location.reload()
    }
});

