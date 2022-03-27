import React from "react";
import "./styles/navibar.css"

export function Navibar() {
    return (
        <ul>
            <li><a class="active" href="">Home</a></li>
            <li><a href="">Users</a></li>
            <li><a href="">Projects</a></li>
            <li><a href="">To do notes</a></li>
        </ul>
    )
}

export default Navibar