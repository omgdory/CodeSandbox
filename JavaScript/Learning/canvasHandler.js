const c = document.getElementById("thaCanvas");
const ctx = c.getContext("2d");

function getMerit() {
    const imgReference = document.getElementById("meritpic")
    const img = new Image();
    img.src = imgReference.src;
    
    let widthInt = imgReference.clientWidth;
    let heightInt = imgReference.clientHeight;
    let aspect = heightInt / widthInt;

    const newWidth = 200;
    const newHeight = newWidth*aspect

    ctx.drawImage(img, 10, 10, newWidth, newHeight);
}
