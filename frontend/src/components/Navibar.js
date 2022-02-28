import React from "react";
import {Button, Nav, Navbar} from "react-bootstrap";
import {Link} from "react-router-dom";



export function NaviBar() {
    return (
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Navbar.Brand>To do app</Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav"/>
            <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link><Link to='/users/'>Users </Link></Nav.Link>
                    <Nav.Link><Link to='/todo/'>To Do </Link></Nav.Link>
                    <Nav.Link><Link to='/project/'>Projects </Link></Nav.Link>
                    {/*{this.is_auth() ? <button onClick={() => this.logout()}>Logout<button>*/}
                        <Nav.Link><Link to='/login/'>Login</Link></Nav.Link>
                            {/*}*/}
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    )
}

export default NaviBar