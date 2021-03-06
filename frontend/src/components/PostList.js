import React, { Component } from 'react'
import axios from 'axios'

class PostList extends Component {

    constructor(props) {
        super(props)

        this.state = {
            posts: []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/posts/')
        .then(res => {
            console.log(res)
            this.setState({
                posts: res.data
            });
            // setimages(res.data)
        })
        .catch(err => {
            console.log(err)
        })
    }

    render() {
        const { posts } = this.state
        return (
            <div>
                <h1>List Of posts</h1>
                {
                    posts.length ?
                    posts.map(post => <div key = {post.id}>{post.title}</div>) :
                    null
                    

                }
            </div>
        )
    }
}

export default PostList