"use strict";

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

var Human = /*#__PURE__*/function () {
  function Human(name, age) {
    _classCallCheck(this, Human);

    this.name = name;
    this.age = age;
  }

  _createClass(Human, [{
    key: "sayHelloTo",
    value: function sayHelloTo(somebody) {
      return "Hello, ".concat(somebody, "! I'm ").concat(this.name);
    }
  }]);

  return Human;
}();

var arrowFunc = function arrowFunc(arg) {
  "This is arrow func with arg: ".concat(arg);
};

var some = arrowFunc(5);
console.log(some);