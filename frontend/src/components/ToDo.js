import React from "react";

const ToDoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.project}</td>
            <td>{todo.note_text}</td>
            <td>{todo.created_at}</td>
            <td>{todo.updated_at}</td>
            <td>{todo.is_active}</td>
            <td>{todo.users.username}</td>
        </tr>
    )
}

const ToDoList = ({todo_list}) => {
    return (
        <table>
            <tr>
                <th>Project name</th>
                <th>Note text</th>
                <th>Created</th>
                <th>Updated</th>
                <th>Active</th>
                <th>User</th>
            </tr>
            {todo_list.map(todo => <ToDoItem todo={todo}/>)}
        </table>
    )
}

export default ToDoList