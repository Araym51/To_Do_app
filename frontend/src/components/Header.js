import React from "react";
import {Card} from "react-bootstrap";

export function CardHeader() {
    return (
        <Card>
            <Card.Header>
                Card.Header
            </Card.Header>
            <Card.Body>
                <Card.Title>
                    Card.Title
                </Card.Title>
                <Card.Text>
                    Card.Text
                </Card.Text>
            </Card.Body>
        </Card>

    )
}

export default CardHeader