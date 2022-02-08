import React from "react";
import {Container} from "react-bootstrap";

// компонент для отображения футера:
export function Footer() {
    return (
            <Container fluid style={{backgroundColor: '#212529', color: '#fff'}}>
                <Container style={{
                    display: "flex",
                    justifyContent: "center",
                    padding: "10px",
                    height: "60px",
                }}>
                    <p>To do app</p>
                </Container>
            </Container>
    )
}

export default Footer
