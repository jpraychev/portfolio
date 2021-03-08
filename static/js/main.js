// TO DO - Move these functions to a separate file and import them when needed
const removeActive = () => {
    $('#sidebar').removeClass('active')
    $('.arrow').removeClass('left').addClass('right')
}

const addActive = () => {
    $('#sidebar').addClass('active')
    $('.arrow').removeClass('right').addClass('left')
}

const checkWidth = (width) => {
    return width > 768 ? true : false;
}

$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('.arrow').toggleClass('left right');
    });
    
    checkWidth($(document).width()) ? '' : removeActive();
});

$(window).on("resize", function() {

    width = $(this).width();
    checkWidth(width) ? addActive() : removeActive();

});