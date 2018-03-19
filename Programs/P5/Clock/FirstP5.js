function setup() {
  createCanvas(600,600,)
  angleMode(DEGREES)

}
function draw() {
  background(255)
  translate(300,300)
  rotate(-90)

  var s = second()
  var m = minute()
  var h = hour()
  var mi = millis()

  noFill()
  arc(0,0,390,390,0,s*6)
  stroke(100,255,200)
  strokeWeight(30)

  noFill()
  arc(0,0,320,320,0,m*6)
  stroke(255,100,100)
  strokeWeight(30)

  noFill()
  arc(0,0,250,250,0,h*30)
  stroke(100,200,255)
  strokeWeight(30)



}
