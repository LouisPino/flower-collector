document.addEventListener("DOMContentLoaded", function () {
    var elems = document.querySelectorAll(".materialboxed");
    var instances = M.Materialbox.init(elems);
});
console.log('hit');

function myFunction() {
    alert("Hello from a static file!");
  }