import React, {useEffect, useState} from "react";
import {useQuery} from "@apollo/client";
import {GET_ALL_USERS} from "../query/users";


const UsersList = ({users_list}) => {
    const {data, loading, error} = useQuery(GET_ALL_USERS)
    const [users, setUsers] = useState([])
    console.log(data)

    useEffect(() => {
        if (!loading) {
            setUsers(data.users)
        }
    }, [data])
    if (loading) {
        return <h1>Loading...</h1>
    }
    return (
        <table>
            <th>user id</th>
            <th>username</th>
            <th>firstname</th>
            <th>lastname</th>
            <th>email</th>
            {users.map(user =>
                <tr>
                    <td>{user.id}.</td>
                    <td>{user.username}</td>
                    <td>{user.firstName}</td>
                    <td>{user.lastName} </td>
                    <td>{user.email}</td>
                </tr>
            )}
        </table>)
}

export default UsersList