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
            match.forEach(post => {
                console.log(post.title)
            });
            
        });
    };
    displayData();
});