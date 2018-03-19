function truck(x,y) {
  this.x = x;
  this.y = y;
  this.xdir = 0;
  this.ydir = 7;
  console.log("truck",this.x,this.y);

  this.show = function() {
   image(img2,this.x,this.y,100,190)
/*    rect(this.x,this.y,100,190)
    noStroke()
    fill(0,255,0)*/
  }

  this.move = function() {
    this.x = this.x + this.xdir;
    this.y = this.y + this.ydir;
  }

}
