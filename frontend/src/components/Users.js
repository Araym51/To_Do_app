import React from "react";

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

const UsersList = ({users_list}) => {
    return (
        <table>
            <th>
                | User name |
            </th>
            <th>
                | User email |
            </th>
            <th>
                | User first name|
            </th>
            <th>
                | User last name |
            </th>
            {users_list.map((users_app) => <UsersItem users_app={users_app} />)}
        </table>
    )
}

export default UsersList
