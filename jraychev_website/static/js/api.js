// All API calls
const postsURL = 'http://localhost:8000/api/v1/posts'

const getPosts = async (url) => {
    const postsResponse = await fetch(url);
    const postsData = await postsResponse.json();
    return postsData
}

$("#search-bar").on('click', function(){
    const displayData = async () => {
        const postsObject = await getPosts(postsURL)
        const posts = postsObject.posts
        
        $("#search-bar").keyup(function(){
            let searchData = $(this).val().toLowerCase();
            const match = posts.filter(post => {
                const result = post.title.toLowerCase().includes(searchData)
                return result
            })
            // const html = match.map(post =>`
            //     <li><a href="${post.id}">${post.title}</a>
            //     <a class="float-right small text-secondary" href="${post.category__name}"> in ${post.category__name}</a></li>`
            // ).join('');
            const html = match.map(post => 
                "<li>\
                    <a href="+getBaseUrl('')+""+post.id+">"+post.title+"</a>\
                    <a class='float-right small text-secondary' href="+getBaseUrl('category')+""+post.category__name+">in "+post.category__name+"</a>\
                </li>").join('')
            $(".dropdown-content").html(html);
        });
    };
    displayData();
});

function removeSearchStyle() {
    $(".dropdown-content").removeClass('show');
    $("#search-bar").removeClass('style-search-bar');
};

function addSearchStyle() {
    $(".dropdown-content").toggleClass('show');
    $("#search-bar").toggleClass('style-search-bar');
};
/** 
* Function returns base url for post or category view
* @param {string} url - Function accepts a string URL for paramter. If none is specified, base url for posts is used.\
Note that the parameter for this function has to be identical to the one in posts/urls.py in order for the function to work properly.
* @return {string} Returns the base url for a specified parameter
*
* Basic usage:
* getBaseUrl() => Base URL for posts view
* getBaseUrl('category') => Base URL for category view. 
*/
const getBaseUrl  = (url = 'posts') => {
    const httpBaseUrl = $(".dropdown-content").attr("data-url");
    const httpPostsPath = $(".dropdown-content").attr("data-posts-href")
    const httpCatPath = $(".dropdown-content").attr("data-cat-href")
    const categoryUrl = httpCatPath.substring(0,httpCatPath.length-2)
    var baseUrl = `${httpBaseUrl}${httpPostsPath}`
    
    if (url === 'category') {
        baseUrl = `${httpBaseUrl}${categoryUrl}`
    }
    return baseUrl
}

$(window).on("click", function(event){
    const clickedElemenet = event.target;
    const searchBar = $("#search-bar")[0];
    clickedElemenet == searchBar ? addSearchStyle() : removeSearchStyle();
})

$('#email-button').on('click', function() {
    // Get the value from email-address input
    const userEmail = $('#email-address').val()
    $('#email-address').val('')
    const csrfToken = $("input[name='csrfmiddlewaretoken']").val()
    const cookies = document.cookie
    const url = 'http://localhost:8000/api/v1/subscribe/'

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/x-www-form-urlencoded");
    myHeaders.append("Cookie", cookies);

    var urlencoded = new URLSearchParams();
    urlencoded.append('email', userEmail);
    urlencoded.append('csrfmiddlewaretoken', csrfToken);
    
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: urlencoded,
        redirect: 'follow'
    };
    
    fetch(url, requestOptions)
      .then(response => response.text())
      .then(result => console.log(result))
      .catch(error => console.log('error', error));

});

/** 
* Returns browser cookies
* @summary Return browser cookies in form of an object if function parameters is not specified or returns a single entry from that object
* @param {string} cookie - Specify a cookie to be returned or leave empty /function call/ to get all cookies in form of object
* @return {object or string} Returns object or individual cookies
*/

function getCoockies(cookie='') {
    const cookies = document.cookie.split(';')
    var cookieObj = {};

    cookies.forEach(cookie => {
        var keyValuePair = cookie.split('=')
        var key = keyValuePair[0].trim()
        var value = keyValuePair[1].trim()
        cookieObj[key] = value
    });

    if (cookie === '') { return cookieObj }
    if (cookie in cookieObj) { return cookieObj[cookie]}
    
    return new Error('There is no such cookies stored in the browser')
}