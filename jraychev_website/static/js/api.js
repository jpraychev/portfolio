// All API calls
const postsURL = 'http://localhost:8000/api/v1/posts'

const getPosts = async (url) => {
    const postsResponse = await fetch(url);
    const postsData = await postsResponse.json();
    return postsData
}

$("#search-bar").on('click', function(){
    console.log('Searh bar clicked. Starting data download...78.7-72.5')

    const displayData = async () => {
        const postsObject = await getPosts(postsURL)
        const posts = postsObject.posts
        
        $("#search-bar").keyup(function(){
            let searchData = $(this).val().toLowerCase();
            const match = posts.filter(post => {
                const result = post.title.toLowerCase().includes(searchData)
                return result
            })
            const html = match.map(post =>`
                <li><a href="${post.id}">${post.title}</a>
                <a class="float-right" href="${post.category__name}">in ${post.category__name}</a></li>`
            ).join('');
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

const getBaseUrl  = () => {
    const httpBaseUrl = $(".dropdown-content").attr("data-url");
    const httpPath = $(".dropdown-content").attr("data-href") 
    const baseUrl = `${httpBaseUrl}${httpPath}`.split('/')
    console.log(baseUrl)
}

getBaseUrl()

$(window).on("click", function(event){
    const clickedElemenet = event.target;
    const searchBar = $("#search-bar")[0];
    clickedElemenet == searchBar ? addSearchStyle() : removeSearchStyle();
})