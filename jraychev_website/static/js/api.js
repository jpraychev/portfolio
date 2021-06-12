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