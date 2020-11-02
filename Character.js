//character draw

class Character {   //ES6

    constructor(x,y, step, image1, image2) {
        this._image_a = new Image();
        this._image_a.src = image1;

        this._image_b = new Image();
        this._image_b.src = image2;


        this.x = x;
        this.y = y;

        this._switch = true;
        this._step = step;

    }

    addX(){
        this.x = this.x + this._step;
    }

    getImage() {
        this._switch = !this._switch;
        return (this._switch) ? this._image_a : this._image_b;
        }
    }

