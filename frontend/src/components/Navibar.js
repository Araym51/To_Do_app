import React from "react";
import {HashRouter, Link} from "react-router-dom";
import "./styles/navibar.css"

export function Navibar() {
    return (
        <ul>
            <HashRouter>
                <li><Link to='/'>Home</Link></li>
                {/*<li><Link to='login/'><a>Login</a></Link></li>*/}
                <li><Link to='users/'>Users</Link></li>
                <li><Link to='projects/'>Projects</Link></li>
                <li><Link to='todo/'>To do notes</Link></li>
            </HashRouter>
        </ul>
    )
}

export default Navibar