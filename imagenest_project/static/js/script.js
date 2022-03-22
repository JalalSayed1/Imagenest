
function like(id) {

    // e.preventDefault();

    // each image has a unique id, therefore has a unique like button with id = eg. #likeBtn4
    var elt = document.querySelector("#likeBtn" + id);
    elt.classList.toggle("black_and_white");

    if (!elt.classList) {
        var classes = elt.className.split(" ");
        var i = classes.indexOf("black_and_white");
    }

}




// like this post by submitting the like form:
$(document).on('submit', '#like_button_form', function (e) {
    // don't do default behaviour when submitting this form (liking an image):
    e.preventDefault();
    $.ajax({
        type: 'POST',
        data: {
            task: $("#like_image_input").val(),
            // submit the form (like an image):
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
    })
});
