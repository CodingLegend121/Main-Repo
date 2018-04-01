var car;
var trucks = [];
var trucks2 = [];
var score = 1
var scoreAdd = 1
var Speed = 6
var diff = 'Easy'

function preload() {
  img = loadImage('baby_crawling.jpg');
  img2 = loadImage('toy_block.png');
}

function setup() {
  title = headize(createP('Car Game'), 20, 0)
  normal = headize(createP(diff), 60, 100)

  createCanvas(600, 700);
  car = new car();
  trucks = truckArray(trucks, -180)
  console.log(trucks[0].x, trucks[0].y)
  truck2 = truckArray(trucks2, -680)
}

function draw() {
  background(130, 100, 60);
  car.show();
  //drawLine(200, 0, 200, 700)
  //drawLine(400, 0, 400, 700)
  truckDraw(trucks, -180)
  truckDraw(trucks2, -180)
  wallBounce()
  //console.log(trucks.length);
  //console.log("truck 0",car.x+","+car.y+","+trucks[0].x+","+trucks[0].y,dist(car.x,car.y,trucks[0].x,trucks[0].y));
  //if (trucks.length > 1)
  //      console.log("truck 1",car.x+","+car.y+","+trucks[1].x+","+trucks[1].y,dist(car.x,car.y,trucks[1].x,trucks[1].y));
  //alert("");
  // if (car.hits(trucks || trucks2)) {
  truckHit(trucks)
  truckHit(trucks2)
  score = score + scoreAdd
  //scoreText = headize(createP('Score - ' + score), 20, 150)
}


function headize(word, x, y) {
  word.style('font-size', '60px')
  word.position(x, y)
  word.style('font-family', 'Verdana')

}

function keyPressed() {
  if (keyCode === RIGHT_ARROW) {
    car.move(1)
  } else if (keyCode === LEFT_ARROW) {
    car.move(-1)
  }
}

function drawLine(x1, y1, x2, y2) {
  stroke(150)
  strokeWeight(20)
  line(x1, y1, x2, y2)
}

function wallBounce() {
  if (car.x > 450) {
    car.x = 450;
  } else if (car.x < 50) {
    car.x = 50;
  }
}

function truckArray(truk, num) {
  for (var i = 0; i < 2; i++) {
    truk[i] = new truck(i * 200 + random([50, 250]), num, Speed);
    console.log("truckArray", truk[i].x, truk[i].y);
  }
  return truk;
}

function truckDraw(draw, n) {
  for (var i = 0; i < draw.length; i++) {
    draw[i].show();
    draw[i].move();
    if (draw[i].y > 880) {
      draw[i].y = n;
      for (var j = 0; j < random([1, 2, 0]); j++) {
        draw[i].x = j * 200 + random([50, 250]);
        draw[i].y = n
      }
    }
  }
}

function truckHit(t) {
  if (dist(car.x, car.y, t[0].x, t[0].y) <= 184) {
    //  console.log("HITS");
    alert("HIT - " + score);
    location.reload();
  }

  if (t.length > 1) {
    if (dist(car.x, car.y, t[1].x, t[1].y) <= 184) {
      //  console.log("HITS");
      alert("HIT - " + score);
      location.reload();
    }
  }
}