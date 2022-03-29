import React from "react";
import {Link} from "react-router-dom";
import "./styles/navibar.css"

export function Navibar() {
    return (
        <ul>
            <li><a href='/'>Home</a></li>
            {/*<li><Link to='login/'><a>Login</a></Link></li>*/}
            <li><a href='/users'>Users</a></li>
            <li><a href='/projects'>Projects</a></li>
            <li><a href='/todo'>To do notes</a></li>
        </ul>
    )
}

export default Navibar