import React from "react";

const UsersItem = ({users}) => {
    return (
        <tr>
            <td>
                {users.username}
            </td>
            <td>
                {users.email}
            </td>
            <td>
                {users.first_name}
            </td>
            <td>
                {users.last_name}
            </td>
        </tr>
    )
}

const UsersList = ({users_list}) => {
    return (
        <table>
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
            {users_list.map((users) => <UsersItem users={users} />)}
        </table>
    )
}

export default UsersList


