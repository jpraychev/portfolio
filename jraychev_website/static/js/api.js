// Hold function for all API requests

const postsURL = 'http://localhost:8000/api/v1/posts'

const getPosts = async (url) => {
    const postsResponse = await fetch(url);
    const postsData = await postsResponse.json();
    return postsData
}

const displayPosts = async (data) => {
    const postObject = await getPosts(postsURL)
    const posts = postObject.posts
    // console.log(posts)
    
    // Create a regex and search if the typed from user input is in the title of the text
    
    const match = posts.filter(post => {
        const result = post.title.toLowerCase().includes(data.toLowerCase())
        return result
        // return post.title.includes(data);
    })
    try {
        console.log(`${match[0].title} in ${match[0].category__name}`)
    } catch {
        console.log('No results')
    }
    // console.log(match[0].title)
}
// Call display Posts
// displayPosts()  

$("#search-bar").keyup(function(){
    let searchData = $(this).val();
    displayPosts(searchData)
});
