// Getting the CSRF token
function getcookie(name) {
    const doc_cookie = `; ${document.cookie}`;
    const parts = doc_cookie.split(`; ${name}=`);
    if(parts.length == 2) return parts.pop().split(";").shift();
}

// Update change in edits to posts
function submit_edit(id) {
    const txtarea = document.getElementById(`textarea_${id}`).value;
    const content = document.getElementById(`content_${id}`);
    const modal = document.getElementById(`modal_edit_${id}`);
    fetch(`/edit/${id}`, {
        method: "POST",
        headers: {"Content-type": "application/json", "X-CSRFToken": getcookie("csrftoken")},
        body: JSON.stringify({
            content: txtarea
        })
    })
    .then(response => response.json())
    .then(result => {
        // Change content of textarea in modal based on edited input
        content.innerHTML = result.data;
        // Close off modal pop-up after edit
        // Change modal state like in hidden modal
        modal.classList.remove('show');
        modal.setAttribute('aria-hidden', 'true');
        modal.setAttribute('style', 'display: none');
        // Get modal backdrops
        const modalsBackdrops = document.getElementsByClassName('modal-backdrop');
        // Remove every modal backdrop
        for(let i=0; i<modalsBackdrops.length; i++) {
           document.body.removeChild(modalsBackdrops[i]);
        }
    })
}

// Update likes for posts
function submit_like(id, userpost_like) {
    // Check if id of post exists within list of posts liked by user. If id exists within list, position of element returned will be valid.
    if(userpost_like.indexOf(id) >= 0) {
        var likedpost = true;
    }
    else {
        var likedpost = false;
    }

    // Remove class of like/unlike button and add back later without needing for refresh
    const likebtn = document.getElementById(`${id}`);
    const likeword = document.getElementById(`like_${id}`);
    likebtn.classList.remove('fa-thumbs-up');
    likebtn.classList.remove('fa-thumbs-down');
    likeword.innerHTML = " ";

    // Remove like status if true and vice versa
    if(likedpost === true) {
        fetch(`/removelike/${id}`)
        .then(response => response.json())
        .then(result => {
            likebtn.classList.add('fa-thumbs-up');
            likeword.innerHTML = "Like";
            likedpost = false;
        })
    }
    else {
        fetch(`/addlike/${id}`)
        .then(response => response.json())
        .then(result => {
            likebtn.classList.add('fa-thumbs-down');
            likeword.innerHTML = "Unlike";
            likedpost = true;
        })
    }
}
