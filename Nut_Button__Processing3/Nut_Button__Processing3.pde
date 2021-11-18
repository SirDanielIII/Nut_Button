import ddf.minim.*;
import ddf.minim.analysis.*;
import ddf.minim.effects.*;
import ddf.minim.signals.*;
import ddf.minim.spi.*;
import ddf.minim.ugens.*;

Minim minim;
AudioSample Nut;

void setup() {
  size(1000, 1000);
  background(0);
  circle(width/2, height/2, 1000);
  textSize(400);
  fill(0);
  text("Nut", 150, 625);
  minim = new Minim(this);
  Nut = minim.loadSample("Nut.wav", 512);
}

void draw() {
}

void mousePressed() {
  if (dist(mouseX, mouseY, 500, 500 ) < 500) {
    Nut.trigger();
  }
}
