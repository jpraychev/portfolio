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

    // Toggles sidebar
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('.arrow').toggleClass('left right');
    });
    
    // Checks if width is bigger than 768 px
    checkWidth($(document).width()) ? '' : removeActive();

    // Renders social box on contact page
    $('.social-box-animate').animate({ 
        left: '0%',
        opacity: '1'
    }, 750 );

    // Renders contact form on contact page
    $('.contact-form-animate').animate({ 
        right: '0%',
        opacity: '1'
    }, 750 );

    for (let i=1; i<4; i++) {
        var delaySeconds = 500+i*450;

        $('.fadeInUp-'+ i +'').animate({
            'bottom': '0'
        }, delaySeconds );

        $('.fadeInRight-'+ i +'').animate({ 
            'margin-left': '0%',
            'opacity': '1'
        }, delaySeconds );
    };

    

});

// Hides or shows the sidebar based on size of window
$(window).on('resize', function() {
    
    width = $(this).width();
    checkWidth(width) ? addActive() : removeActive();

});

