$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('.arrow').toggleClass('left right');
    });

    if ( $(document).width() > 768 ) {
    } else {
        $('#sidebar').removeClass('active')
        $('.arrow').toggleClass('left right')
    }

    $(window).on("resize", function(event){
        width = $(this).width();

        if ( width > 768 ) {
            $('#sidebar').addClass('active')
            $('.arrow').removeClass('right')
            $('.arrow').addClass('left')
        } else {
            $('#sidebar').removeClass('active')
            $('.arrow').removeClass('left')
            $('.arrow').addClass('right')    
        }
    });
});
