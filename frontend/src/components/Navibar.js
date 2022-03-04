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
                    <Nav.Link>
                        {this.is_auth() ? <Button variant="dark" onClick={() => this.logout()}>Logout</Button> :
                            <Button variant="dark"><Link to='/login/'>Login</Link></Button>}
                    </Nav.Link>}
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    )
}

export default NaviBar