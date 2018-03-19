function setup() {
  createCanvas(700,400);
}
function draw() {
  background(0,200,200)
  platform()
  ball(350,355)
  // console.log(mouseX,mouseY);
}
function platform() {
  rect(-1,350,701,50)
  stroke(200,120,0)
  fill(230,150,0)
}
function ball(x,y) {
  ellipse(x,y,40)
  stroke(0,130,0)
  fill(0,160,0)
  strokeWeight(7)
}
function keyPressed() {
  if(key == true){
    console.log('I did it');
  }
}
