import React from "react";
import "./styles/navibar.css"

export function Navibar(logout) {
    let username = localStorage.getItem('login')
    let login_button = ''
    if (username != '') {
        login_button = <div><li><a href='/'> Hello {username}!</a></li>
            <li><button onClick={logout}> Logout </button></li></div>
    } else {
        login_button = <a href='/login'>Login</a>
    }
    console.log('username', username)
    return (
        <ul>
            <li><a href='/'>Home</a></li>
            <li><a href='/users'>Users</a></li>
            <li><a href='/projects'>Projects</a></li>
            <li><a href='/todo'>To do notes</a></li>
            <li>{login_button}</li>

        </ul>
    )
}

export default Navibar