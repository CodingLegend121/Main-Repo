var tilesheet;
var tiledata;
var tiles =[]
function preload() {
  tiledata = loadJSON('tiles/tiles.json')
  tilesheet = loadImage("tiles/tiles_spritesheet.png")
}

function setup(){
  createCanvas(500,500)
  let frames = tiledata.tiles;
  for (let i = 0; i < frames.length; i++) {
    let pos = frames[i].pos;
    let img = tilesheet.get(pos.x, pos.y, pos.width, pos.height);
    tiles.push(img);
  }
  console.log(tiledata);
}
function draw(){
  background(51)
  drawBlock(55,0,450)
  drawBlock(56,50,450)
  drawBlock(43,100,450)

}

function drawBlock(i,x,y) {
  image(tiles[i],x,y,50,50)
}
