import React from "react";
import {Table} from "react-bootstrap";

// собираем данные с api:
const UsersItem = ({users_app}) => {
    return (
        <tr>
            <td>
                {users_app.username}
            </td>
            <td>
                {users_app.email}
            </td>
            <td>
                {users_app.first_name}
            </td>
            <td>
                {users_app.last_name}
            </td>
        </tr>
    )
}

// формируем таблицу:
const UsersList = ({users_list}) => {
    return (
            <Table striped bordered hover>
                <th>
                    User name
                </th>
                <th>
                    User email
                </th>
                <th>
                    User first name
                </th>
                <th>
                    User last name
                </th>
                {users_list.map((users_app) => <UsersItem users_app={users_app}/>)}
            </Table>
    )
}

export default UsersList
