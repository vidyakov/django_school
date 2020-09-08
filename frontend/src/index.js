class Human {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    sayHelloTo (somebody) {
        return `Hello, ${somebody}! I'm ${this.name}`
    }
}


let arrowFunc = (arg) => {`This is arrow func with arg: ${arg}`};
let some = arrowFunc(5);
console.log(some);
