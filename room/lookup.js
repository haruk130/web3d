
var ltsin = [];
var ltcos = [];
for (let i=-360;i<=360;i++) {
    ltsin.push(sin(i));
    ltcos.push(cos(i));
}

function sin(z) {
    return Math.sin(z*(Math.PI/180));
}
function cos(z) {
    return Math.cos(z*(Math.PI/180));
}

function lsin(z) {
    idx = Math.floor(z%360);
    console.log(z,idx)
    return [ltsin[idx+360],sin(z)];
}
console.log(lsin(0))
console.log(lsin(1))
console.log(lsin(-1))
console.log(lsin(90))
console.log(lsin(100))
console.log(lsin(180))
console.log(lsin(-270))
console.log(lsin(540))
console.log(lsin(-180))

console.log(2*Math.PI*(180/Math.PI))