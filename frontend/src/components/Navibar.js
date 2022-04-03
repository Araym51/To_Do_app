import React from "react";
import "./styles/navibar.css"

export function Navibar(auth, logout) {
    let login_button = ''
    if (auth.is_login) {
        login_button = <button className="btn btn-outline-success my-2 my-sm-0"
                               onClick={logout}>Hello, {auth.username} Logout</button>
    } else {
        login_button = <a href='/login'>Login</a>
    }
    return (
        <ul>
            <li><a href='/'>Home</a></li>
            <li>{login_button}</li>
            <li><a href='/users'>Users</a></li>
            <li><a href='/projects'>Projects</a></li>
            <li><a href='/todo'>To do notes</a></li>
        </ul>
    )
}

export default Navibar