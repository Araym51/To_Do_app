import React, {useEffect, useState} from "react";
import {useQuery} from "@apollo/client";
import {GET_ALL_TODO} from "../query/todo";

const ToDoList = () => {
    const {data, loading, error} = useQuery(GET_ALL_TODO)
    const [toDos, setToDo] = useState([])

    useEffect(() => {
        if (!loading) {
            setToDo(data.toDo)
        }
    }, [data])
    if (loading) {
        return <h1>Loading...</h1>
    }
    return (
        <table>
            <th>Project</th>
            <th>Note text</th>
            <th>users</th>
            <th>created at</th>
            <th>updated at</th>
            <th>Active</th>
            {toDos.map(toDo =>
                <tr>
                    <td>{toDo.project.project}</td>
                    <td>{toDo.noteText}</td>
                    <td>{toDo.users.username}</td>
                    <td>{toDo.createdAt}</td>
                    <td>{toDo.updatedAt}</td>
                    <td>{toDo.isActive}</td>
                </tr>
            )}
        </table>
    )
}

export default ToDoList