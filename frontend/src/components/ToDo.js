import React from "react";
import {Table} from "react-bootstrap";

const ToDoItem = ({todo, deleteToDo}) => {
    return(
        <tr>
            <td>{todo.project}</td>
            <td>{todo.note_text}</td>
            {/*<td>{todo.users}</td> пересмотреть сериализатор*/}
            <td>{todo.created_at}</td>
            <td>{todo.updated_at}</td>
            <td>{todo.is_active}</td>
            {/*<td><button onClick={()=> deleteToDo(todo.id)} type='button'>Delete</button></td> сделать флаг is_active: False*/}
        </tr>
    )
}

const ToDoList = ({todo_list, deleteToDo}) => {
    return (
        <Table striped bordered hover>
            <th>Project name</th>
            <th>Note text</th>
            {/*<th>User</th>*/}
            <th>Created</th>
            <th>Updated</th>
            <th>Active</th>
            {todo_list.map((todo) => <ToDoItem todo={todo} /> )} {/*deleteToDo = {deleteToDo}*/}
        </Table>
    )
}

export default ToDoList