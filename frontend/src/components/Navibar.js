import React from "react";
import {Button, Nav, Navbar} from "react-bootstrap";

export function NaviBar() {
    return (
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Navbar.Brand>To do app</Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav"/>
            <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link >Users</Nav.Link>
                    <Nav.Link >Projects</Nav.Link>
                    <Nav.Link >ToDo</Nav.Link>
                </Nav>
                {/*<Nav>*/}
                {/*    <Button variant="primary" className="mr-2">Авторизация</Button>*/}
                {/*    <Button variant="primary" className="mr-2">Выход</Button>*/}
                {/*</Nav>*/}
            </Navbar.Collapse>
        </Navbar>
    )
}

export default NaviBar