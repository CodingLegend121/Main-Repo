function car() {
  this.x = 250;
  this.y = 500


  this.show = function() {
    image(img,this.x,this.y,100,175)
/*    rect(this.x,this.y,100,175)
    noStroke()
    noFill()*/
  }
  this.move = function(dir) {
    this.x += dir*200;
  }
/*  this.hits =function(truck) {
    var d = dist(this.x,this.y,truck.x,truck.y)
    if (d<0) {
        return true;
    } else {
       return false;*/


}
