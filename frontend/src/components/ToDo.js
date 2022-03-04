import React from "react";
import {Table} from "react-bootstrap";

const ToDoItem = ({todo}) => {
    return(
        <tr>
            <td>{todo.project}</td>
            <td>{todo.note_text}</td>
            <td>{todo.users}</td>
            <td>{todo.created_at}</td>
            <td>{todo.updated_at}</td>
            <td>{todo.is_active}</td>
        </tr>
    )
}

const ToDoList = ({todo_list}) => {
    return (
        <Table striped bordered hover>
            <th>
                Project name
            </th>
            <th>
                Note text
            </th>
            <th>
                User
            </th>
            <th>
                Created
            </th>
            <th>
                Updated
            </th>
            <th>
                Active
            </th>
            {todo_list.map((todo) => <ToDoItem todo={todo} /> )}
        </Table>
    )
}

export default ToDoList