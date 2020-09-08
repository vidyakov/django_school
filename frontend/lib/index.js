class Human {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  sayHelloTo(somebody) {
    return `Hello, ${somebody}! I'm ${this.name}`;
  }

}