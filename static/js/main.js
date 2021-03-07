$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('.arrow').toggleClass('left right');
    });
    
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
    
    if ( checkWidth($(document).width()) == false ) {
        removeActive()
    }

    $(window).on("resize", function() {

        width = $(this).width();
    
        checkWidth(width) ? addActive() : removeActive();
        
    });
});
