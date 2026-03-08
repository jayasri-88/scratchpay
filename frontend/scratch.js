const canvas = document.getElementById("scratchCard");
const ctx = canvas.getContext("2d");

canvas.width = 300;
canvas.height = 150;

ctx.fillStyle = "gray";
ctx.fillRect(0,0,300,150);

let scratching = false;

canvas.addEventListener("mousedown",()=>{
scratching=true;
});

canvas.addEventListener("mouseup",()=>{
scratching=false;
reveal();
});

canvas.addEventListener("mousemove",(e)=>{

if(!scratching) return;

let rect = canvas.getBoundingClientRect();

let x = e.clientX - rect.left;
let y = e.clientY - rect.top;

ctx.clearRect(x,y,20,20);

});

function reveal(){

let params = new URLSearchParams(window.location.search);

let code = params.get("code");

let upi = document.getElementById("upi").value;

fetch("http://127.0.0.1:5000/scratch/"+code,{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
upi_id:upi
})
})
.then(res=>res.json())
.then(data=>{

document.getElementById("result").innerText =
"You won ₹"+data.reward;

});

}