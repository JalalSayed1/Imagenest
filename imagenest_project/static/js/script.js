// $(document).ready(function () {
//     $("#like-btn").click(function () {

//         $('.black_and_white').on('change', toggle);

//     });
// });

// function toggle() {
//     $('.black_and_white').toggleClass("black_and_white");
// }

function like(id) {
    
    // event.preventDefault();
    
    // each image has a unique id, therefore has a unique like button with id = eg. #likeBtn4
    var elt = document.querySelector("#likeBtn"+id);
    elt.classList.toggle("black_and_white");
    
    if (!element.classList) {
        var classes = elt.className.split(" ");
        var i = classes.indexOf("black_and_white");
    }

}