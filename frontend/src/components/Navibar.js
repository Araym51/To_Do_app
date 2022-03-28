import React from "react";
import {HashRouter, Link} from "react-router-dom";
import "./styles/navibar.css"

export function Navibar() {
    return (
        <HashRouter>
        <ul>
            <li><Link to='/'><a class="active">Home</a></Link></li>
            {/*<li><Link to='login/'><a>Login</a></Link></li>*/}
            <li><Link to='users/'><a>Users</a></Link></li>
            <li><Link to='projects/'><a>Projects</a></Link></li>
            <li><Link to='todo/'><a>To do notes</a></Link></li>
        </ul>
            </HashRouter>
    )
}

export default Navibar